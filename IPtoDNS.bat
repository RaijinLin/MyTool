@echo off
setlocal EnableDelayedExpansion

set output_file=output.txt

for /f "tokens=*" %%a in (input.txt) do (
    set "ip=%%a"
    echo Domain names for !ip!:
    for /f "tokens=*" %%b in ('nslookup !ip! ^| findstr /i "name"') do (
        set "line=%%b"
        for /f "tokens=2" %%c in ("!line!") do (
            echo %%c >> !output_file!
        )
    )
    echo. >> !output_file!
)

echo Output written to file: !output_file!
