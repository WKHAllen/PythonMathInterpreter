# -*- mode: python -*-

block_cipher = None


a = Analysis(['MathInterpreter2.0.py'],
             pathex=['C:\\Users\\Will\\Desktop\\Programming\\PyCpp\\Python Math Interpreter\\2.0'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             win_no_prefer_redirects=None,
             win_private_assemblies=None,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          Tree('data', prefix='data'),
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='MathInterpreter2.0',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='icon.ico')
