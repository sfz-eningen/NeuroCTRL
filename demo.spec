# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['demo.py'],
             pathex=['M:\\Projekte\\SFZ\\GIT\\NeuroCTRL'],
             binaries=[],
             datas=[('C:\\Users\\beimg\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\site-packages\\scipy\\sparse\\linalg\\isolve\\_iterative.cp37-win32.pyd', 'site-packages\\scipy\\sparse\\linalg\\isolve'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\.gitattributes', '.'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\.gitignore', '.'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\AITEST.py', '.'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\demo.py', '.'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\demo.spec', '.'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\install.py', '.'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\LICENSE', '.'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\mam.py', '.'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\python37.dll', '.'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\README.md', '.'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\record.py', '.'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\requirements.txt', '.'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\settings.py', '.'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\start.py', '.'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\t.py', '.'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\TODO.md', '.'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\__init__.py', '.'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\.vscode', '.vscode/'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\AI', 'AI/'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\aiprep', 'aiprep/'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\api', 'api/'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\basic_libs', 'basic_libs/'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\build-files', 'build-files/'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\cli', 'cli/'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\communication', 'communication/'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\config', 'config/'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\external_lib', 'external_lib/'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\samples', 'samples/'), ('M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\test_generator', 'test_generator/')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='demo',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='M:\\Projekte\\SFZ\\GIT\\NeuroCTRL\\build-files\\icon.ico')
