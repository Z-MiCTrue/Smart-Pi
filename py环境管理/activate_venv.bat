cd /d %~dp0

call NLP\Scripts\activate
python -m pip install --upgrade pip

:loop
set /p cmd=command:
%cmd%
goto loop
