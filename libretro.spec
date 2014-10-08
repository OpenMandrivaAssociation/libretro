# Debug depends on system CFLAGS but various cores use their own
# It's quite a pain to patch every core for CFLAGS and maintain patches
# And debug is not really needed here anyway
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	An interface for emulator and game ports
Name:		libretro
Version:	20141007
Release:	2
# Actually, various for each core but mostly GPLv2
License:	GPL
Group:		Emulators
Url:		http://www.libretro.org/
# fetched via libretro-fetch.sh from git and re-packed
Source0:	%{name}-%{version}.tar.bz2
Source1:	mupen64plus-libretro-1.git.20140916.tar.xz
# Disable inlining for VBA Next to fix build
Patch0:		libretro-20141007-vba-next-inline.patch
# Enable 4DO build
Patch1:		libretro-20141007-build-4do.patch
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(zlib)
Suggests:	retroarch
Suggests:	%{name}-4do
Suggests:	%{name}-bluemsx
Suggests:	%{name}-bnes
Suggests:	%{name}-bsnes-accuracy
Suggests:	%{name}-bsnes-balanced
Suggests:	%{name}-bsnes-performance
Suggests:	%{name}-bsnes-mercury-accuracy
Suggests:	%{name}-bsnes-mercury-balanced
Suggests:	%{name}-bsnes-mercury-performance
Suggests:	%{name}-desmume
Suggests:	%{name}-dosbox
Suggests:	%{name}-fba
Suggests:	%{name}-fceumm
Suggests:	%{name}-fmsx
Suggests:	%{name}-gambatte
Suggests:	%{name}-genesis-plus-gx
Suggests:	%{name}-handy
Suggests:	%{name}-mednafen-gba
Suggests:	%{name}-mednafen-lynx
Suggests:	%{name}-mednafen-ngp
Suggests:	%{name}-mednafen-pcfx
Suggests:	%{name}-mednafen-psx
Suggests:	%{name}-mednafen-snes
Suggests:	%{name}-mednafen-supergrafx
Suggests:	%{name}-mednafen-vb
Suggests:	%{name}-mednafen-wswan
Suggests:	%{name}-meteor
Suggests:	%{name}-mupen64plus
Suggests:	%{name}-nestopia
Suggests:	%{name}-nxengine
Suggests:	%{name}-o2em
Suggests:	%{name}-pcsx-rearmed
Suggests:	%{name}-ppsspp
Suggests:	%{name}-prboom
Suggests:	%{name}-prosystem
Suggests:	%{name}-quicknes
Suggests:	%{name}-scummvm
Suggests:	%{name}-snes9x
Suggests:	%{name}-snes9x-next
Suggests:	%{name}-stella
Suggests:	%{name}-tgbdual
Suggests:	%{name}-tyrquake
Suggests:	%{name}-vba-next
Suggests:	%{name}-vbam
Suggests:	%{name}-vecx
Suggests:	%{name}-virtualjaguar
Suggests:	%{name}-yabause

%description
For each emulator 'core', RetroArch makes use of a library API that we like
to call 'libretro'.

Think of libretro as an interface for emulator and game ports. You can make
a libretro port once and expect the same code to run on all the platforms
that RetroArch supports. It's designed with simplicity and ease of use in
mind so that the porter can worry about the port at hand instead of having
to wrestle with an obfuscatory API.

The purpose of the project is to help ease the work of the emulator/game
porter by giving him an API that allows him to target multiple platforms
at once without having to redo any code. He doesn't have to worry about
writing input/video/audio drivers - all of that is supplied to him by
RetroArch. All he has to do is to have the emulator port hook into the
libretro API and that's it - we take care of the rest.

%files

#----------------------------------------------------------------------------

%package 4do
Summary:	4DO core for libretro (3DO)
Provides:	libretro-core = %{EVRD}
Suggests:	bchunk

%description 4do
4DO core for libretro. It's used to run Panasonic 3DO games.

It requires 3DO BIOS (panafz10.bin) so place it in your RetroArch/libretro
"System Directory" folder.

It also needs images to be in .iso format so you may need bchunk to convert
bin/cue to .iso:

bchunk old_image.bin old_image.cue new_image.iso

%files 4do
%{_libdir}/%{name}/4do_libretro.info
%{_libdir}/%{name}/4do_libretro.so

#----------------------------------------------------------------------------

%package bluemsx
Summary:	blueMSX core for libretro (MSX)
Provides:	libretro-core = %{EVRD}

%description bluemsx
blueMSX core for libretro. It's used to run MSX games.

This core requires the two folders named Machines/ and Databases/ from
standalone blueMSX copied inside your frontend's system directory. You
can get these from the official Windows standalone version of blueMSX
( http://www.bluemsx.com/ ) or any other binary package.

%files bluemsx
%{_libdir}/%{name}/bluemsx_libretro.info
%{_libdir}/%{name}/bluemsx_libretro.so

#----------------------------------------------------------------------------

%package bnes
Summary:	bNES core for libretro (NES)
Provides:	libretro-core = %{EVRD}

%description bnes
bNES core for libretro. It's used to run Nintendo games.

%files bnes
%{_libdir}/%{name}/bnes_libretro.info
%{_libdir}/%{name}/bnes_libretro.so

#----------------------------------------------------------------------------

%package bsnes-accuracy
Summary:	bSNES core for libretro with accuracy optimization (SNES)
Provides:	libretro-core = %{EVRD}

%description bsnes-accuracy
bSNES core for libretro with accuracy optimization.
It's used to run Super Nintendo games.

%files bsnes-accuracy
%{_libdir}/%{name}/bsnes_accuracy_libretro.info
%{_libdir}/%{name}/bsnes_accuracy_libretro.so

#----------------------------------------------------------------------------

%package bsnes-balanced
Summary:	bSNES core for libretro with balanced optimization (SNES)
Provides:	libretro-core = %{EVRD}

%description bsnes-balanced
bSNES core for libretro with balanced optimization.
It's used to run Super Nintendo games.

%files bsnes-balanced
%{_libdir}/%{name}/bsnes_balanced_libretro.info
%{_libdir}/%{name}/bsnes_balanced_libretro.so

#----------------------------------------------------------------------------

%package bsnes-performance
Summary:	bSNES core for libretro with performance optimization (SNES)
Provides:	libretro-core = %{EVRD}

%description bsnes-performance
bSNES core for libretro with performance optimization.
It's used to run Super Nintendo games.

%files bsnes-performance
%{_libdir}/%{name}/bsnes_performance_libretro.info
%{_libdir}/%{name}/bsnes_performance_libretro.so

#----------------------------------------------------------------------------

%package bsnes-mercury-accuracy
Summary:	bSNES-Mercury core for libretro with accuracy optimization (SNES)
Provides:	libretro-core = %{EVRD}

%description bsnes-mercury-accuracy
bSNES-Mercury core for libretro with accuracy optimization.
It's used to run Super Nintendo games.

bSNES-Mercury is a fork of Higan, aiming to restore some useful features that
have been removed, as well as improving performance a bit. Maximum accuracy is
still uncompromisable; anything that affects accuracy is optional and off by
default.

Changes to upstream:
- The biggest change is getting the interface sane, which is accomplished
  through libretro.
- Another change is the restoration of HLE emulation of some special chips,
  to improve performance and reduce reliance on those chip ROMs (they're not
  really easy to find). Chips for which no HLE emulation was developed
  (ST-0011 and ST-0018) are still LLE.
- A seven-line function in sfc/memory/memory-inline.hpp was replaced, which
  speeds up ROM load by roughly a factor 6 (1.2s -> 0.2s).
- A section in sfc/memory/memory.cpp was specialized for the common, easy,
  case. This speeds up ROM load time by about a third.
- A fast path was added to various parts of the CPU bus, improving framerate
  by about 2.5%.
- 'inline' was added all across the PPU subclasses. Framerate went up by 20%
  from such a trivial change!

%files bsnes-mercury-accuracy
%{_libdir}/%{name}/bsnes_mercury_accuracy_libretro.info
%{_libdir}/%{name}/bsnes_mercury_accuracy_libretro.so

#----------------------------------------------------------------------------

%package bsnes-mercury-balanced
Summary:	bSNES-Mercury core for libretro with balanced optimization (SNES)
Provides:	libretro-core = %{EVRD}

%description bsnes-mercury-balanced
bSNES-Mercury core for libretro with balanced optimization.
It's used to run Super Nintendo games.

bSNES-Mercury is a fork of Higan, aiming to restore some useful features that
have been removed, as well as improving performance a bit. Maximum accuracy is
still uncompromisable; anything that affects accuracy is optional and off by
default.

Changes to upstream:
- The biggest change is getting the interface sane, which is accomplished
  through libretro.
- Another change is the restoration of HLE emulation of some special chips,
  to improve performance and reduce reliance on those chip ROMs (they're not
  really easy to find). Chips for which no HLE emulation was developed
  (ST-0011 and ST-0018) are still LLE.
- A seven-line function in sfc/memory/memory-inline.hpp was replaced, which
  speeds up ROM load by roughly a factor 6 (1.2s -> 0.2s).
- A section in sfc/memory/memory.cpp was specialized for the common, easy,
  case. This speeds up ROM load time by about a third.
- A fast path was added to various parts of the CPU bus, improving framerate
  by about 2.5%.
- 'inline' was added all across the PPU subclasses. Framerate went up by 20%
  from such a trivial change!

%files bsnes-mercury-balanced
%{_libdir}/%{name}/bsnes_mercury_balanced_libretro.info
%{_libdir}/%{name}/bsnes_mercury_balanced_libretro.so

#----------------------------------------------------------------------------

%package bsnes-mercury-performance
Summary:	bSNES-Mercury core for libretro with performance optimization (SNES)
Provides:	libretro-core = %{EVRD}

%description bsnes-mercury-performance
bSNES-Mercury core for libretro with performance optimization.
It's used to run Super Nintendo games.

bSNES-Mercury is a fork of Higan, aiming to restore some useful features that
have been removed, as well as improving performance a bit. Maximum accuracy is
still uncompromisable; anything that affects accuracy is optional and off by
default.

Changes to upstream:
- The biggest change is getting the interface sane, which is accomplished
  through libretro.
- Another change is the restoration of HLE emulation of some special chips,
  to improve performance and reduce reliance on those chip ROMs (they're not
  really easy to find). Chips for which no HLE emulation was developed
  (ST-0011 and ST-0018) are still LLE.
- A seven-line function in sfc/memory/memory-inline.hpp was replaced, which
  speeds up ROM load by roughly a factor 6 (1.2s -> 0.2s).
- A section in sfc/memory/memory.cpp was specialized for the common, easy,
  case. This speeds up ROM load time by about a third.
- A fast path was added to various parts of the CPU bus, improving framerate
  by about 2.5%.
- 'inline' was added all across the PPU subclasses. Framerate went up by 20%
  from such a trivial change!

%files bsnes-mercury-performance
%{_libdir}/%{name}/bsnes_mercury_performance_libretro.info
%{_libdir}/%{name}/bsnes_mercury_performance_libretro.so

#----------------------------------------------------------------------------

%package desmume
Summary:	Desmume core for libretro (NDS)
Provides:	libretro-core = %{EVRD}

%description desmume
Desmume core for libretro. It's used to run Nintendo DS games.

%files desmume
%{_libdir}/%{name}/desmume_libretro.info
%{_libdir}/%{name}/desmume_libretro.so

#----------------------------------------------------------------------------

%package dosbox
Summary:	DOSBox core for libretro (DOS)
Provides:	libretro-core = %{EVRD}

%description dosbox
DOSBox core for libretro. It's used to run DOS games.

%files dosbox
%{_libdir}/%{name}/dosbox_libretro.info
%{_libdir}/%{name}/dosbox_libretro.so

#----------------------------------------------------------------------------

%package fba
Summary:	Final Burn Alpha core for libretro (arcade)
Provides:	libretro-core = %{EVRD}

%description fba
Final Burn Alpha core for libretro. It's used to run arcade games.

It should be able to load:
- Capcom CPS-1 and CPS-2
- SNK Neo-Geo
- Toaplan
- Cave hardware
- and various games on miscellaneous hardware

%files fba
%{_libdir}/%{name}/fb_alpha_libretro.info
%{_libdir}/%{name}/fb_alpha_libretro.so

#----------------------------------------------------------------------------

%package fceumm
Summary:	FCE Ultra mappers modified core for libretro (NES)
Provides:	libretro-core = %{EVRD}

%description fceumm
FCE Ultra mappers modified core for libretro. It's used to run Nintendo games.

%files fceumm
%{_libdir}/%{name}/fceumm_libretro.info
%{_libdir}/%{name}/fceumm_libretro.so

#----------------------------------------------------------------------------

%package fmsx
Summary:	fMSX core for libretro (MSX)
Provides:	libretro-core = %{EVRD}

%description fmsx
fMSX core for libretro. It's used to run MSX games.

%files fmsx
%{_libdir}/%{name}/fmsx_libretro.info
%{_libdir}/%{name}/fmsx_libretro.so

#----------------------------------------------------------------------------

%package gambatte
Summary:	Gambatte core for libretro (GBC)
Provides:	libretro-core = %{EVRD}

%description gambatte
Gambatte core for libretro. It's used to run Game Boy Color games.

%files gambatte
%{_libdir}/%{name}/gambatte_libretro.info
%{_libdir}/%{name}/gambatte_libretro.so

#----------------------------------------------------------------------------

%package genesis-plus-gx
Summary:	Genesis Plus GX core for libretro (SMD etc)
Provides:	libretro-core = %{EVRD}

%description genesis-plus-gx
Genesis Plus GX core for libretro. It should be able to load:
- Genesis/Mega Drive
- Sega/Mega CD
- Master System
- Game Gear & SG-1000

%files genesis-plus-gx
%{_libdir}/%{name}/genesis_plus_gx_libretro.info
%{_libdir}/%{name}/genesis_plus_gx_libretro.so

#----------------------------------------------------------------------------

%package handy
Summary:	Handy core for libretro (LNX)
Provides:	libretro-core = %{EVRD}

%description handy
Handy core for libretro. It's used to run Atari Lynx games.

%files handy
%{_libdir}/%{name}/handy_libretro.info
%{_libdir}/%{name}/handy_libretro.so

#----------------------------------------------------------------------------

%package mednafen-gba
Summary:	Mednafen Game Boy Advance core for libretro (GBA)
Provides:	libretro-core = %{EVRD}

%description mednafen-gba
Mednafen GBA core for libretro. It's used to run Game Boy Advance games.

%files mednafen-gba
%{_libdir}/%{name}/mednafen_gba_libretro.info
%{_libdir}/%{name}/mednafen_gba_libretro.so

#----------------------------------------------------------------------------

%package mednafen-lynx
Summary:	Mednafen Lynx core for libretro (LNX)
Provides:	libretro-core = %{EVRD}

%description mednafen-lynx
Mednafen Lynx core for libretro. It's used to run Atari Lynx games.

%files mednafen-lynx
%{_libdir}/%{name}/mednafen_lynx_libretro.info
%{_libdir}/%{name}/mednafen_lynx_libretro.so

#----------------------------------------------------------------------------

%package mednafen-ngp
Summary:	Mednafen Neo Geo Pocket core for libretro (NGP)
Provides:	libretro-core = %{EVRD}

%description mednafen-ngp
Mednafen NGP core for libretro. It's used to run Neo Geo Pocket games.

%files mednafen-ngp
%{_libdir}/%{name}/mednafen_ngp_libretro.info
%{_libdir}/%{name}/mednafen_ngp_libretro.so

#----------------------------------------------------------------------------

%package mednafen-pce
Summary:	Mednafen PC Engine core for libretro (PCE)
Provides:	libretro-core = %{EVRD}

%description mednafen-pce
Mednafen PCE core for libretro. It's used to run PC Engine/TurboGrafx-16 games.

TG-CD emulation requires the CD BIOS image, named as syscard3.pce.
This BIOS image is to be placed into the Mednafen base directory ~/.mednafen/.
Then, you will have to indicate to Mednafen where the syscard3.pce file is
located. To do this, edit the ~/.mednafen/mednafen.cfg file:

;Path to the ROM BIOS

pce.cdbios /path/to/file/syscard3.pce

%files mednafen-pce
%{_libdir}/%{name}/mednafen_pce_fast_libretro.info
%{_libdir}/%{name}/mednafen_pce_fast_libretro.so

#----------------------------------------------------------------------------

%package mednafen-pcfx
Summary:	Mednafen PC-FX core for libretro (PC-FX)
Provides:	libretro-core = %{EVRD}

%description mednafen-pcfx
Mednafen PC-FX core for libretro. It's used to run PC-FX games.

%files mednafen-pcfx
%{_libdir}/%{name}/mednafen_pcfx_libretro.info
%{_libdir}/%{name}/mednafen_pcfx_libretro.so

#----------------------------------------------------------------------------

%package mednafen-psx
Summary:	Mednafen Sony Playstation 1 core for libretro (PSX)
Provides:	libretro-core = %{EVRD}

%description mednafen-psx
Mednafen PSX core for libretro. It's used to run Sony Playstation 1 games.

* Running

To run this core, the "system directory" must be defined if running in
RetroArch. Here, the PSX BIOSes must be placed, $sysdir/SCPH550{0,1,2}
for Japanese, NA and EU regions respectively. Memory cards will also be
saved to this system directory.

* Loading ISOs

Mednafen differs from other PS1 emulators in that it reads a .cue sheet
that points to an .iso/.bin whatever. If you have e.g. <tt>foo.iso</tt>,
you should create a foo.cue, and fill this in:

    FILE "foo.iso" BINARY
       TRACK 01 MODE1/2352
          INDEX 01 00:00:00

After that, you can load the <tt>foo.cue</tt> file as a ROM.
Note that this is a dirty hack and will not work on all games.
Ideally, make sure to use rips that have cue-sheets.

%files mednafen-psx
%{_libdir}/%{name}/mednafen_psx_libretro.info
%{_libdir}/%{name}/mednafen_psx_libretro.so

#----------------------------------------------------------------------------

%package mednafen-snes
Summary:	Mednafen Super Nintendo core for libretro (SNES)
Provides:	libretro-core = %{EVRD}

%description mednafen-snes
Mednafen SNES core for libretro. It's used to run Super Nintendo games.

%files mednafen-snes
%{_libdir}/%{name}/mednafen_snes_libretro.info
%{_libdir}/%{name}/mednafen_snes_libretro.so

#----------------------------------------------------------------------------

%package mednafen-supergrafx
Summary:	Mednafen SuperGrafx core for libretro (PCE)
Provides:	libretro-core = %{EVRD}

%description mednafen-supergrafx
Mednafen SuperGrafx core for libretro. It's used to run PC Engine SuperGrafx
games.

%files mednafen-supergrafx
%{_libdir}/%{name}/mednafen_supergrafx_libretro.info
%{_libdir}/%{name}/mednafen_supergrafx_libretro.so

#----------------------------------------------------------------------------

%package mednafen-vb
Summary:	Mednafen Virtual Boy core for libretro
Provides:	libretro-core = %{EVRD}

%description mednafen-vb
Mednafen VB core for libretro. It's used to run Nintendo Virtual Boy games.

%files mednafen-vb
%{_libdir}/%{name}/mednafen_vb_libretro.info
%{_libdir}/%{name}/mednafen_vb_libretro.so

#----------------------------------------------------------------------------

%package mednafen-wswan
Summary:	Mednafen WonderSwan core for libretro
Provides:	libretro-core = %{EVRD}

%description mednafen-wswan
Mednafen WSwan core for libretro. It's used to run Bandai WonderSwan games.

%files mednafen-wswan
%{_libdir}/%{name}/mednafen_wswan_libretro.info
%{_libdir}/%{name}/mednafen_wswan_libretro.so

#----------------------------------------------------------------------------

%package meteor
Summary:	Meteor core for libretro (GBA)
Provides:	libretro-core = %{EVRD}

%description meteor
Meteor core for libretro. It's used to run Game Boy Advance games.

%files meteor
%{_libdir}/%{name}/meteor_libretro.info
%{_libdir}/%{name}/meteor_libretro.so

#----------------------------------------------------------------------------

%package mupen64plus
Summary:	Mupen64 Plus core for libretro (N64)
Provides:	libretro-core = %{EVRD}

%description mupen64plus
Mupen64 Plus core for libretro. It's used to run Nintendo 64 games.

%files mupen64plus
%{_libdir}/%{name}/mupen64plus_libretro.info
%{_libdir}/%{name}/mupen64plus_libretro.so

#----------------------------------------------------------------------------

%package nestopia
Summary:	Nestopia core for libretro (NES)
Provides:	libretro-core = %{EVRD}

%description nestopia
Nestopia core for libretro. It's used to run Nintendo games.

%files nestopia
%{_libdir}/%{name}/nestopia_libretro.info
%{_libdir}/%{name}/nestopia_libretro.so

#----------------------------------------------------------------------------

%package nxengine
Summary:	NXEngine core for libretro (Cave Story)
Provides:	libretro-core = %{EVRD}

%description nxengine
NXEngine core for libretro. It's used to run Cave Story (Doukutsu Monogatari).

%files nxengine
%{_libdir}/%{name}/nxengine_libretro.info
%{_libdir}/%{name}/nxengine_libretro.so

#----------------------------------------------------------------------------

%package o2em
Summary:	O2EM core for libretro (Odyssey 2)
Provides:	libretro-core = %{EVRD}

%description o2em
O2EM core for libretro. It's used to run Magnavox Odyssey 2 & Videopac+ games.

Place "o2rom.bin" in your RetroArch/libretro "System Directory" folder.

%files o2em
%{_libdir}/%{name}/o2em_libretro.info
%{_libdir}/%{name}/o2em_libretro.so

#----------------------------------------------------------------------------

%package pcsx-rearmed
Summary:	PCSX-ReARMed core for libretro (PSX)
Provides:	libretro-core = %{EVRD}

%description pcsx-rearmed
PCSX-ReARMed core for libretro. It's used to run Sony Playstation 1 games.

%files pcsx-rearmed
%{_libdir}/%{name}/pcsx_rearmed_libretro.info
%{_libdir}/%{name}/pcsx_rearmed_libretro.so

#----------------------------------------------------------------------------

%package ppsspp
Summary:	PPSSPP core for libretro (PSP)
Provides:	libretro-core = %{EVRD}

%description ppsspp
PPSSPP core for libretro. It's used to run Sony Playstation Portable games.

%files ppsspp
%{_libdir}/%{name}/ppsspp_libretro.info
%{_libdir}/%{name}/ppsspp_libretro.so
%dir %attr(0777,root,root) %{_libdir}/%{name}/PPSSPP
%{_libdir}/%{name}/PPSSPP/*

#----------------------------------------------------------------------------

%package prboom
Summary:	PrBoom core for libretro (Doom)
Provides:	libretro-core = %{EVRD}

%description prboom
PrBoom core for libretro. It's used to run early Doom games.

PrBoom is a game engine - it provides a program to play Doom levels, but
it doesn't include any levels itself. More importantly, you need all the
sounds, sprites, and other graphics that make up the Doom environment.
So to play PrBoom, you need one of the main Doom date files from id
Software - either doom.wad, doom2.wad, tnt.wad or plutonia.wad from one
of the commercial Doom games, or the shareware doom1.wad. This file
is called the IWAD.

PrBoom also supports playing Doom add-on levels, called "PWADs", which
are small extra .wad files which just contain extra levels or other
resources. PWADs are ONLY ADD-ONS, you still need the original IWAD
that they are designed to work with. In practice, most PWADs on the
Internet require doom2.wad (although some work with doom.wad).

%files prboom
%{_libdir}/%{name}/prboom_libretro.info
%{_libdir}/%{name}/prboom_libretro.so

#----------------------------------------------------------------------------

%package prosystem
Summary:	ProSystem core for libretro (Atari 7800)
Provides:	libretro-core = %{EVRD}

%description prosystem
ProSystem core for libretro. It's used to run Atari 7800 ProSystem games.

Place "ProSystem.dat" (required) and "7800 BIOS (U).rom" (optional) in your
RetroArch/libretro "System Directory" folder.

Or just set "System Directory" to %{_libdir}/%{name}/prosystem/

%files prosystem
%{_libdir}/%{name}/prosystem_libretro.info
%{_libdir}/%{name}/prosystem_libretro.so
%dir %attr(0777,root,root) %{_libdir}/%{name}/prosystem
%{_libdir}/%{name}/prosystem/ProSystem.dat

#----------------------------------------------------------------------------

%package quicknes
Summary:	QuickNES core for libretro (NES)
Provides:	libretro-core = %{EVRD}

%description quicknes
QuickNES core for libretro. It's used to run Nintendo games.

%files quicknes
%{_libdir}/%{name}/quicknes_libretro.info
%{_libdir}/%{name}/quicknes_libretro.so

#----------------------------------------------------------------------------

%package scummvm
Summary:	ScummVM core for libretro (DOS etc)
Provides:	libretro-core = %{EVRD}

%description scummvm
ScummVM core for libretro. It's used to run various games,
mostly classic DOS point-and-click adventures.

%files scummvm
%{_libdir}/%{name}/scummvm_libretro.info
%{_libdir}/%{name}/scummvm_libretro.so

#----------------------------------------------------------------------------

%package snes9x
Summary:	SNES9x core for libretro (SNES)
Provides:	libretro-core = %{EVRD}

%description snes9x
SNES9x core for libretro. It's used to run Super Nintendo games.

%files snes9x
%{_libdir}/%{name}/snes9x_libretro.info
%{_libdir}/%{name}/snes9x_libretro.so

#----------------------------------------------------------------------------

%package snes9x-next
Summary:	SNES9x Next core for libretro (SNES)
Provides:	libretro-core = %{EVRD}

%description snes9x-next
SNES9x Next core for libretro. It's used to run Super Nintendo games.

SNES9x Next is an optimized port/rewrite of SNES9x 1.52+ to libretro.

%files snes9x-next
%{_libdir}/%{name}/snes9x_next_libretro.info
%{_libdir}/%{name}/snes9x_next_libretro.so

#----------------------------------------------------------------------------

%package stella
Summary:	Stella core for libretro (Atari 2600)
Provides:	libretro-core = %{EVRD}

%description stella
Stella core for libretro. It's used to run Atari 2600 games.

%files stella
%{_libdir}/%{name}/stella_libretro.info
%{_libdir}/%{name}/stella_libretro.so

#----------------------------------------------------------------------------

%package tgbdual
Summary:	TGB Dual core for libretro (GBC)
Provides:	libretro-core = %{EVRD}

%description tgbdual
TGB Dual core for libretro. It's used to run Game Boy and Game Boy Color games.

%files tgbdual
%{_libdir}/%{name}/tgbdual_libretro.info
%{_libdir}/%{name}/tgbdual_libretro.so

#----------------------------------------------------------------------------

%package tyrquake
Summary:	Tyr-Quake core for libretro (Quake)
Provides:	libretro-core = %{EVRD}

%description tyrquake
Tyr-Quake core for libretro. It's used to run Quake 1 and QuakeWorld.

%files tyrquake
%{_libdir}/%{name}/tyrquake_libretro.info
%{_libdir}/%{name}/tyrquake_libretro.so

#----------------------------------------------------------------------------

%package vba-next
Summary:	VBA Next core for libretro (GBA)
Provides:	libretro-core = %{EVRD}

%description vba-next
VBA Next core for libretro. It's used to run Game Boy Advance games.

VBA Next is an optimized port of VBA-M to libretro.

%files vba-next
%{_libdir}/%{name}/vba_next_libretro.info
%{_libdir}/%{name}/vba_next_libretro.so

#----------------------------------------------------------------------------

%package vbam
Summary:	VBA-M core for libretro (GBA)
Provides:	libretro-core = %{EVRD}

%description vbam
VBA-M core for libretro. It's used to run Game Boy Advance games.

%files vbam
%{_libdir}/%{name}/vbam_libretro.info
%{_libdir}/%{name}/vbam_libretro.so

#----------------------------------------------------------------------------

%package vecx
Summary:	VECX core for libretro (Vectrex)
Provides:	libretro-core = %{EVRD}

%description vecx
VECX core for libretro. It's used to run Vectrex games.

The original Vectrex games are freely available for non-commercial use.

%files vecx
%{_libdir}/%{name}/vecx_libretro.info
%{_libdir}/%{name}/vecx_libretro.so

#----------------------------------------------------------------------------

%package virtualjaguar
Summary:	Virtual Jaguar core for libretro (JAG)
Provides:	libretro-core = %{EVRD}

%description virtualjaguar
Virtual Jaguar core for libretro. It's used to run Atari Jaguar games.

%files virtualjaguar
%{_libdir}/%{name}/virtualjaguar_libretro.info
%{_libdir}/%{name}/virtualjaguar_libretro.so

#----------------------------------------------------------------------------

%package yabause
Summary:	Yabause core for libretro (Sega Saturn)
Provides:	libretro-core = %{EVRD}

%description yabause
Yabause core for libretro. It's used to run Sega Saturn games.

%files yabause
%{_libdir}/%{name}/yabause_libretro.info
%{_libdir}/%{name}/yabause_libretro.so

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1
# Remove these after fetching to make tarball smaller
# Virtual memory exhausted during build
# rm -rf libretro-picodrive
# Not ready yet
# rm -rf libretro-hatari
# rm -rf libretro-mame
# rm -rf libretro-mame078
# rm -rf libretro-mame139
# rm -rf libretro-uae
# Just not needed
# rm -rf libretro-bsnes_cplusplus98
# rm -rf libretro-2048
# rm -rf libretro-3dengine
# rm -rf libretro-dinothawr

rm -rf libretro-mupen64plus
tar -xf %{SOURCE1}
mv mupen64plus-libretro-1.git.20140916 libretro-mupen64plus

%build
./libretro-build.sh

%install
mkdir -p %{buildroot}%{_libdir}/%{name}
./libretro-install.sh %{buildroot}%{_libdir}/%{name}

# ProSystem system files
mkdir -p %{buildroot}%{_libdir}/%{name}/prosystem/
install -m 0644 libretro-prosystem/ProSystem.dat %{buildroot}%{_libdir}/%{name}/prosystem/ProSystem.dat

# PPSSPP system files
mkdir -p %{buildroot}%{_libdir}/%{name}/PPSSPP/
cp -a libretro-ppsspp/lang %{buildroot}%{_libdir}/%{name}/PPSSPP/
cp -a libretro-ppsspp/flash0 %{buildroot}%{_libdir}/%{name}/PPSSPP/
cp -a libretro-ppsspp/assets/shaders %{buildroot}%{_libdir}/%{name}/PPSSPP/
cp -a libretro-ppsspp/assets/* %{buildroot}%{_libdir}/%{name}/PPSSPP/

# Remove installed info files that we don't use yet
rm -f %{buildroot}%{_libdir}/%{name}/2048_libretro.info
rm -f %{buildroot}%{_libdir}/%{name}/3dengine_libretro.info
rm -f %{buildroot}%{_libdir}/%{name}/bsnes_cplusplus98_libretro.info
rm -f %{buildroot}%{_libdir}/%{name}/dinothawr_libretro.info
rm -f %{buildroot}%{_libdir}/%{name}/fba_cores_cps1_libretro.info
rm -f %{buildroot}%{_libdir}/%{name}/fba_cores_cps2_libretro.info
rm -f %{buildroot}%{_libdir}/%{name}/fba_cores_neo_libretro.info
rm -f %{buildroot}%{_libdir}/%{name}/ffmpeg_libretro.info
rm -f %{buildroot}%{_libdir}/%{name}/hatari_libretro.info
rm -f %{buildroot}%{_libdir}/%{name}/imame4all_libretro.info
rm -f %{buildroot}%{_libdir}/%{name}/mame078_libretro.info
rm -f %{buildroot}%{_libdir}/%{name}/mame2010_libretro.info
rm -f %{buildroot}%{_libdir}/%{name}/mame_libretro.info
rm -f %{buildroot}%{_libdir}/%{name}/mess_libretro.info
rm -f %{buildroot}%{_libdir}/%{name}/pcsx_rearmed_interpreter_libretro.info
rm -f %{buildroot}%{_libdir}/%{name}/pcsx_rearmed_libretro_neon.info
rm -f %{buildroot}%{_libdir}/%{name}/picodrive_libretro.info
rm -f %{buildroot}%{_libdir}/%{name}/pocketsnes_libretro.info
rm -f %{buildroot}%{_libdir}/%{name}/puae_libretro.info
rm -f %{buildroot}%{_libdir}/%{name}/remotejoy_libretro.info

