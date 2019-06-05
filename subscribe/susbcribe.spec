# -*- mode: python -*-

block_cipher = None


a = Analysis(['D:\\mqtt_vision1\\subscribe\\exes/susbcribe.py'],
             pathex=['D:\\mqtt_vision1\\subscribe'],
             binaries=[],
             datas=[],
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
          name='susbcribe',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , version='D:\\mqtt_vision1\\subscribe\\res\\version.txt', icon='D:\\mqtt_vision1\\subscribe\\res\\logo.ico')
