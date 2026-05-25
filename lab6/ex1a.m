clear;
clc;
close all;

%% Reference conversation
referenceText = "hello can you hear me clearly this is a test conversation between two computers";

%% Recording settings
Fs = 44100;
nBits = 16;
nChannels = 1;
duration = 10;

%% Distance under test
distance = 2;   % meters

%% Record received sound
recObj = audiorecorder(Fs, nBits, nChannels);

disp("Start playing the voice conversation from Machine 1...");
recordblocking(recObj, duration);
disp("Recording finished.");

received_signal = getaudiodata(recObj);

original_filename = "received_" + distance + "m_original.wav";
audiowrite(original_filename, received_signal, Fs);

%% Signal processing: band-pass filter
low_cutoff = 300;
high_cutoff = 3400;

[b, a] = butter(6, [low_cutoff high_cutoff]/(Fs/2), 'bandpass');

filtered_signal = filtfilt(b, a, received_signal);

%% Amplification
gain = 4;
processed_signal = gain * filtered_signal;

% Normalize
processed_signal = processed_signal / max(abs(processed_signal));

processed_filename = "received_" + distance + "m_processed.wav";
audiowrite(processed_filename, processed_signal, Fs);

%% Speech-to-text
transcript = speech2text(processed_signal, Fs);

disp("Reference text:");
disp(referenceText);

disp("Recognized text:");
disp(transcript);

%% Error calculation
wer = wordErrorRateSimple(referenceText, transcript);
wer_percent = wer * 100;

disp("Word Error Rate:");
disp(wer_percent + "%");

%% Plot received and processed signals
t = (0:length(received_signal)-1)/Fs;

figure;
plot(t, received_signal);
xlabel("Time [s]");
ylabel("Amplitude");
title("Original Received Signal at " + distance + " m");
grid on;

figure;
plot(t, processed_signal);
xlabel("Time [s]");
ylabel("Amplitude");
title("Processed Signal at " + distance + " m");
grid on;