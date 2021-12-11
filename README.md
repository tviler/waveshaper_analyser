# Waveshaper analyser

This script analyses the transfer function of a waveshaper by ploting the input against the output. It then tries to curve fit the result with some common functions.

## Windows binary usage:
1. Process "TEST.wav" and export the result as a 16-bit 44.1 kHz file named "RESULT.wav". Make sure the files are time-aligned, eg. have it at the start of the timeline.
2. Place "RESULT.wav" in the same directory as this file. There is an example file included, just overwrite it.
3. Run "RUN.bat" in the same directory as this file.
4. Results are found in the results directory.

## Python 3 script usage:
**Dependencies:**
* numpy 1.21.4
* scipy 1.7.3
* matplotlib 3.5.0

1. Move to the source folder.
2. Process "TEST.wav" and export the result as a 16-bit 44.1 kHz file named "RESULT.wav". Make sure the files are time-aligned, eg. have it at the start of the timeline.
3. Place "RESULT.wav" in the same directory as waveshaper_analysis.py. There is an example file included, just overwrite it.
4. Run the python script, eg. "python waveshaper_analysis.py" in a terminal.
5. Results are found in the results directory.

## About the results
"waveshape.png" displays the transfer function over the full range of the signal.
The curve fitting is only performed on the positive part of the signal. The resulting curves are displayed in "curve_fit.png" and "curve_fit_zoom.png".
"curve_fit.txt" contains the coefficients found by the curve fitting. If the coefficients display "nan" it means the fit failed for that function.

-tviler
