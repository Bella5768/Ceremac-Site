# Script de déploiement complet pour Windows
# Exécutez ce script dans PowerShell

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Déploiement complet CEREMAC" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# 1. Commit et push vers GitHub
Write-Host "`n1. Commit et push vers GitHub..." -ForegroundColor Yellow
git add .
git commit -m "Mise à jour automatique - $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
git push origin main

if ($LASTEXITCODE -ne 0) {
    Write-Host "Erreur lors du push vers GitHub" -ForegroundColor Red
    exit 1
}

Write-Host "✓ Code poussé sur GitHub avec succès" -ForegroundColor Green

# 2. Instructions pour PythonAnywhere
Write-Host "`n2. Instructions pour PythonAnywhere..." -ForegroundColor Yellow
Write-Host "Pour déployer sur PythonAnywhere, vous avez deux options :" -ForegroundColor White
Write-Host ""
Write-Host "Option 1 - Via SSH (automatisé) :" -ForegroundColor Cyan
Write-Host "  - Connectez-vous à PythonAnywhere via SSH"
Write-Host "  - Exécutez: cd ~/Ceremac-Site"
Write-Host "  - Exécutez: git pull"
Write-Host "  - Exécutez: source .venv/bin/activate"
Write-Host "  - Exécutez: python manage.py migrate"
Write-Host "  - Exécutez: python manage.py collectstatic --noinput"
Write-Host "  - Exécutez: python setup_departments_menu.py"
Write-Host "  - Exécutez: python update_services_slugs.py"
Write-Host "  - Redémarrez l'application via l'interface web"
Write-Host ""
Write-Host "Option 2 - Via interface web (manuel) :" -ForegroundColor Cyan
Write-Host "  - Allez sur https://www.pythonanywhere.com/"
Write-Host "  - Ouvrez le console bash"
Write-Host "  - Exécutez les commandes ci-dessus"
Write-Host ""

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Déploiement local terminé !" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Cyan
