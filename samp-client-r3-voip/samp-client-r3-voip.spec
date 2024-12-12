# -*- mode: python ; coding: utf-8 -*-

datas = [
    ('archives/samp-client-r3-voip.zip', 'archives'),
    ('icons/spc.png', 'icons'),
    ('icons/youtube.png', 'icons'),
    ('icons/instagram.png', 'icons'),
    ('icons/discord.png', 'icons'),
    ('icons/github.png', 'icons'),
    ('icons/tiktok.png', 'icons'),
]

a = Analysis(
    ['samp-client-r3-voip.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='samp-client-r3-voip',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icons/ico-spc.ico',
)