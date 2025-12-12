@echo off
REM Script: run_api_report.bat (Versi Final dengan Copy Environment)

set "ALLURE_DIR=allure-results"
set "REPORT_DIR=allure-report"

echo.
echo =========================================================
echo   [1/4] Menjalankan Pytest dan menghasilkan data Allure...
echo =========================================================

REM Menghapus folder hasil mentah Allure sebelumnya (Pytest yang melakukannya)
if exist "%ALLURE_DIR%" rmdir /s /q "%ALLURE_DIR%"

REM Jalankan Pytest. Hasil mentah disimpan di %ALLURE_DIR%
pytest tests/ --alluredir=%ALLURE_DIR%

REM --- [BARIS BARU DITAMBAHKAN] ---
echo.
echo =========================================================
echo   [2/4] Menyalin File Environment dan Executor...
echo =========================================================

REM Menyalin environment.properties dari root ke folder hasil
copy environment.properties "%ALLURE_DIR%"
copy executor.json "%ALLURE_DIR%"

echo.
echo =========================================================
echo   [3/4] Membuat dan Menyimpan Laporan HTML Allure...
echo =========================================================

REM Generate laporan dari data mentah.
allure generate %ALLURE_DIR% -o %REPORT_DIR% --clean
allure serve allure-results
