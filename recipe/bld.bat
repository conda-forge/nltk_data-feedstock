set NLTK_DATA=%PREFIX%\lib\nltk_data
mkdir "%NLTK_DATA%"

robocopy /move /s /fp /nfl /ndl /np %SRC_DIR%\packages %NLTK_DATA%
cd %NLTK_DATA%

forfiles /s /m *.zip /c "cmd /c 7za x -tzip -r -y @file > nul"
