# -*- mode: python -*-

block_cipher = None


a = Analysis(['../../google.py'],
             pathex=['D:\\mycode\\Github\\google-ip-explorer\\pyinstaller-develop\\pyinstaller-develop\\google'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             cipher=block_cipher)
pyz = PYZ(a.pure,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='google.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
