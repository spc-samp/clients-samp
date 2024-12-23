@echo off

echo.
echo Iniciando verificacao de diretorios e arquivos necessarios, em 3 segundos...
timeout /t 3 /nobreak >nul
echo.

echo [/] 10%% Verificando pasta archives...
if not exist "archives" (
    echo [Erro]: A pasta archives nao foi encontrada!
    goto :error
)
timeout /t 2 /nobreak >nul

echo - [Sucesso]: A pasta foi verificada com sucesso!
timeout /t 1 /nobreak >nul
echo.

echo [//] 15%% Verificando arquivo samp-client-r1.zip em archives...
if not exist "archives\samp-client-r1.zip" (
    echo [Erro]: O arquivo samp-client-r1.zip nao foi encontrado em archives!
    goto :error
)
timeout /t 2 /nobreak >nul

echo - [Sucesso]: O arquivo .zip foi verificado com sucesso!
timeout /t 1 /nobreak >nul
echo.

echo [///] 25%% Verificando pasta icons...
if not exist "icons" (
    echo [Erro]: A pasta icons nao foi encontrada!
    goto :error
)
timeout /t 2 /nobreak >nul

echo - [Sucesso]: A pasta foi verificada com sucesso!
timeout /t 1 /nobreak >nul
echo.

echo [////] 30%% Verificando pasta languages em icons...
if not exist "icons\languages" (
    echo [Erro]: A pasta languages nao foi encontrada em icons!
    goto :error
)
timeout /t 2 /nobreak >nul

echo - [Sucesso]: A pasta foi verificada com sucesso!
timeout /t 1 /nobreak >nul
echo.

echo [/////] 35%% Verificando pasta social em icons...
if not exist "icons\social" (
    echo [Erro]: A pasta social nao foi encontrada em icons!
    goto :error
)
timeout /t 2 /nobreak >nul

echo - [Sucesso]: A pasta foi verificada com sucesso!
timeout /t 1 /nobreak >nul
echo.

echo [//////] 45%% Verificando pasta src...
if not exist "src" (
    echo [Erro]: A pasta src nao foi encontrada!
    goto :error
)
timeout /t 2 /nobreak >nul

echo - [Sucesso]: A pasta foi verificada com sucesso!
timeout /t 1 /nobreak >nul
echo.

echo [///////] 55%% Verificando pasta Core em src...
if not exist "src\Core" (
    echo [Erro]: A pasta Core nao foi encontrada em src!
    goto :error
)
timeout /t 2 /nobreak >nul

echo - [Sucesso]: A pasta foi verificada com sucesso!
timeout /t 1 /nobreak >nul
echo.

echo [////////] 65%% Verificando pasta Models em src...
if not exist "src\Models" (
    echo [Erro]: A pasta Models nao foi encontrada em src!
    goto :error
)
timeout /t 2 /nobreak >nul

echo - [Sucesso]: A pasta foi verificada com sucesso!
timeout /t 1 /nobreak >nul
echo.

echo [/////////] 75%% Verificando pasta Services em src...
if not exist "src\Services" (
    echo [Erro]: A pasta Services nao foi encontrada em src!
    goto :error
)
timeout /t 2 /nobreak >nul

echo - [Sucesso]: A pasta foi verificada com sucesso!
timeout /t 1 /nobreak >nul
echo.

echo [//////////] 85%% Verificando pasta UI em src...
if not exist "src\UI" (
    echo [Erro]: A pasta UI nao foi encontrada em src!
    goto :error
)
timeout /t 2 /nobreak >nul

echo - [Sucesso]: A pasta foi verificada com sucesso!
timeout /t 1 /nobreak >nul
echo.

echo [///////////] 95%% Verificando arquivo Main.cs...
if not exist "Main.cs" (
    echo [Erro]: O arquivo Main.cs nao foi encontrado!
    goto :error
)
timeout /t 2 /nobreak >nul

echo - [Sucesso]: O arquivo .cs foi verificada com sucesso!
timeout /t 1 /nobreak >nul

echo.
echo [Sucesso]: Todos os diretorios e arquivos necessarios foram encontrados!
echo.

echo Iniciando compilacao do projeto (samp-client-r1 - SPC) em 5 segundos...
timeout /t 5 /nobreak >nul

echo.
echo Executando comando de compilacao...
echo.

dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true -p:EnableCompressionInSingleFile=true -o ./published
goto :end

:error
echo.
echo [Erro]: A verificacao falhou. Processo de compilacao cancelado!
echo.
pause
exit /b 1

:end
echo.
echo Processo finalizado!
exit /b 0