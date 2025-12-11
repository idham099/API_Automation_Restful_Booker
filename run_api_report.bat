@echo off
set "ALLURE_DIR=allure-results"
set "REPORT_DIR=allure-report"
 
echo   [1/3] Menjalankan Pytest dan menghasilkan data Allure...
echo   ======
if exist "%ALLURE_DIR%" rmdir /s /q "%ALLURE_DIR%"
pytest tests/ --alluredir=%ALLURE_DIR%


echo   [2/3] Membuat dan Menyimpan Laporan HTML Allure...
echo   =====
allure generate %ALLURE_DIR% -o %REPORT_DIR% --clean

echo   [3/3] Membuka Laporan di Browser...
echo   ====
REM Membuka laporan menggunakan Allure open
echo allure serve allure-results

echo   Proses API Automation Selesai. Laporan Allure Terbuka.
