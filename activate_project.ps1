# Permite ejecutar scripts locales en esta sesión
Set-ExecutionPolicy -Scope Process RemoteSigned -Force

# Activa el entorno virtual
& "$PSScriptRoot\venv_311\Scripts\Activate.ps1"
