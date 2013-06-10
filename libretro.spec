# Debug depends on system CFLAGS but various cores use their own
# It's quite a pain to patch every core for CFLAGS and maintain patches
# And debug is not really needed here anyway
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	An interface for emulator and game ports
Name:		libretro
Version:	20130608
Release:	1
Group:		Emulators
# Actually, various for each core but mostly GPLv2
License:	GPL
Url:		http://www.libretro.org/
# fetched via libretro-fetch.sh from git and re-packed
Source:		%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(zlib)
Suggests:	retroarch
Suggests:	%{name}-bnes
Suggests:	%{name}-bsnes-accuracy
Suggests:	%{name}-bsnes-balanced
Suggests:	%{name}-bsnes-performance
Suggests:	%{name}-desmume
Suggests:	%{name}-dosbox
Suggests:	%{name}-fba
Suggests:	%{name}-fceumm
Suggests:	%{name}-gambatte
Suggests:	%{name}-genesis-plus-gx
Suggests:	%{name}-mednafen-gba
Suggests:	%{name}-mednafen-ngp
Suggests:	%{name}-mednafen-psx
Suggests:	%{name}-mednafen-snes
Suggests:	%{name}-mednafen-vb
Suggests:	%{name}-mednafen-wswan
Suggests:	%{name}-meteor
Suggests:	%{name}-nestopia
Suggests:	%{name}-nxengine
Suggests:	%{name}-pcsx-rearmed
Suggests:	%{name}-prboom
Suggests:	%{name}-quicknes
Suggests:	%{name}-scummvm
Suggests:	%{name}-snes9x
Suggests:	%{name}-snes9x-next
Suggests:	%{name}-stella
Suggests:	%{name}-tyrquake
Suggests:	%{name}-vba-next

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

%package bnes
Summary:	bNES core for libretro (NES)
Provides:	libretro-core = %{EVRD}

%description bnes
bNES core for libretro. It's used to run Nintendo games.

%files bnes
%{_libdir}/%{name}/bnes_libretro.so

#----------------------------------------------------------------------------

%package bsnes-accuracy
Summary:	bSNES core for libretro with accuracy optimization (SNES)
Provides:	libretro-core = %{EVRD}

%description bsnes-accuracy
bSNES core for libretro with accuracy optimization.
It's used to run Super Nintendo games.

%files bsnes-accuracy
%{_libdir}/%{name}/bsnes_libretro_accuracy.so

#----------------------------------------------------------------------------

%package bsnes-balanced
Summary:	bSNES core for libretro with balanced optimization (SNES)
Provides:	libretro-core = %{EVRD}

%description bsnes-balanced
bSNES core for libretro with balanced optimization.
It's used to run Super Nintendo games.

%files bsnes-balanced
%{_libdir}/%{name}/bsnes_libretro_balanced.so

#----------------------------------------------------------------------------

%package bsnes-performance
Summary:	bSNES core for libretro with performance optimization (SNES)
Provides:	libretro-core = %{EVRD}

%description bsnes-performance
bSNES core for libretro with performance optimization.
It's used to run Super Nintendo games.

%files bsnes-performance
%{_libdir}/%{name}/bsnes_libretro_performance.so

#----------------------------------------------------------------------------

%package desmume
Summary:	Desmume core for libretro (NDS)
Provides:	libretro-core = %{EVRD}

%description desmume
Desmume core for libretro. It's used to run Nintendo DS games.

%files desmume
%{_libdir}/%{name}/desmume_libretro.so

#----------------------------------------------------------------------------

%package dosbox
Summary:	DOSBox core for libretro (DOS)
Provides:	libretro-core = %{EVRD}

%description dosbox
DOSBox core for libretro. It's used to run DOS games.

%files dosbox
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
%{_libdir}/%{name}/fb_alpha_libretro.so

#----------------------------------------------------------------------------

%package fceumm
Summary:	FCE Ultra mappers modified core for libretro (NES)
Provides:	libretro-core = %{EVRD}

%description fceumm
FCE Ultra mappers modified core for libretro. It's used to run Nintendo games.

%files fceumm
%{_libdir}/%{name}/fceumm_libretro.so

#----------------------------------------------------------------------------

%package gambatte
Summary:	Gambatte core for libretro (GBC)
Provides:	libretro-core = %{EVRD}

%description gambatte
Gambatte core for libretro. It's used to run Game Boy Color games.

%files gambatte
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
%{_libdir}/%{name}/genesis_plus_gx_libretro.so

#----------------------------------------------------------------------------

%package mednafen-gba
Summary:	Mednafen Game Boy Advance core for libretro (GBA)
Provides:	libretro-core = %{EVRD}

%description mednafen-gba
Mednafen GBA core for libretro. It's used to run Game Boy Advance games.

%files mednafen-gba
%{_libdir}/%{name}/mednafen_gba_libretro.so

#----------------------------------------------------------------------------

%package mednafen-ngp
Summary:	Mednafen Neo Geo Pocket core for libretro (NGP)
Provides:	libretro-core = %{EVRD}

%description mednafen-ngp
Mednafen NGP core for libretro. It's used to run Neo Geo Pocket games.

%files mednafen-ngp
%{_libdir}/%{name}/mednafen_ngp_libretro.so

#----------------------------------------------------------------------------

%package mednafen-pce
Summary:	Mednafen PC Engine core for libretro (NGP)
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
%{_libdir}/%{name}/mednafen_pce_fast_libretro.so

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
%{_libdir}/%{name}/mednafen_psx_libretro.so

#----------------------------------------------------------------------------

%package mednafen-snes
Summary:	Mednafen Super Nintendo core for libretro (SNES)
Provides:	libretro-core = %{EVRD}

%description mednafen-snes
Mednafen SNES core for libretro. It's used to run Super Nintendo games.

%files mednafen-snes
%{_libdir}/%{name}/mednafen_snes_libretro.so

#----------------------------------------------------------------------------

%package mednafen-vb
Summary:	Mednafen Virtual Boy core for libretro
Provides:	libretro-core = %{EVRD}

%description mednafen-vb
Mednafen VB core for libretro. It's used to run Nintendo Virtual Boy games.

%files mednafen-vb
%{_libdir}/%{name}/mednafen_vb_libretro.so

#----------------------------------------------------------------------------

%package mednafen-wswan
Summary:	Mednafen WonderSwan core for libretro
Provides:	libretro-core = %{EVRD}

%description mednafen-wswan
Mednafen WSwan core for libretro. It's used to run Bandai WonderSwan games.

%files mednafen-wswan
%{_libdir}/%{name}/mednafen_wswan_libretro.so

#----------------------------------------------------------------------------

%package meteor
Summary:	Meteor core for libretro (GBA)
Provides:	libretro-core = %{EVRD}

%description meteor
Meteor core for libretro. It's used to run Game Boy Advance games.

%files meteor
%{_libdir}/%{name}/meteor_libretro.so

#----------------------------------------------------------------------------

%package nestopia
Summary:	Nestopia core for libretro (NES)
Provides:	libretro-core = %{EVRD}

%description nestopia
Nestopia core for libretro. It's used to run Nintendo games.

%files nestopia
%{_libdir}/%{name}/nestopia_libretro.so

#----------------------------------------------------------------------------

%package nxengine
Summary:	NXEngine core for libretro (Cave Story)
Provides:	libretro-core = %{EVRD}

%description nxengine
NXEngine core for libretro. It's used to run Cave Story (Doukutsu Monogatari).

%files nxengine
%{_libdir}/%{name}/nxengine_libretro.so

#----------------------------------------------------------------------------

%package pcsx-rearmed
Summary:	PCSX-ReARMed core for libretro (PSX)
Provides:	libretro-core = %{EVRD}

%description pcsx-rearmed
PCSX-ReARMed core for libretro. It's used to run Sony Playstation 1 games.

%files pcsx-rearmed
%{_libdir}/%{name}/pcsx_rearmed_libretro.so

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
%{_libdir}/%{name}/prboom_libretro.so

#----------------------------------------------------------------------------

%package quicknes
Summary:	QuickNES core for libretro (NES)
Provides:	libretro-core = %{EVRD}

%description quicknes
QuickNES core for libretro. It's used to run Nintendo games.

%files quicknes
%{_libdir}/%{name}/quicknes_libretro.so

#----------------------------------------------------------------------------

%package scummvm
Summary:	ScummVM core for libretro (DOS etc)
Provides:	libretro-core = %{EVRD}

%description scummvm
ScummVM core for libretro. It's used to run various games,
mostly classic DOS point-and-click adventures.

%files scummvm
%{_libdir}/%{name}/scummvm_libretro.so

#----------------------------------------------------------------------------

%package snes9x
Summary:	SNES9x core for libretro (SNES)
Provides:	libretro-core = %{EVRD}

%description snes9x
SNES9x core for libretro. It's used to run Super Nintendo games.

%files snes9x
%{_libdir}/%{name}/snes9x_libretro.so

#----------------------------------------------------------------------------

%package snes9x-next
Summary:	SNES9x Next core for libretro (SNES)
Provides:	libretro-core = %{EVRD}

%description snes9x-next
SNES9x Next core for libretro. It's used to run Super Nintendo games.

SNES9x Next is an optimized port/rewrite of SNES9x 1.52+ to libretro.

%files snes9x-next
%{_libdir}/%{name}/snes9x_next_libretro.so

#----------------------------------------------------------------------------

%package stella
Summary:	Stella core for libretro (Atari 2600)
Provides:	libretro-core = %{EVRD}

%description stella
Stella core for libretro. It's used to run Atari 2600 games.

%files stella
%{_libdir}/%{name}/stella_libretro.so

#----------------------------------------------------------------------------

%package tyrquake
Summary:	Tyr-Quake core for libretro (Quake)
Provides:	libretro-core = %{EVRD}

%description tyrquake
Tyr-Quake core for libretro. It's used to run Quake 1 and QuakeWorld.

%files tyrquake
%{_libdir}/%{name}/tyrquake_libretro.so

#----------------------------------------------------------------------------

%package vba-next
Summary:	VBA Next core for libretro (GBA)
Provides:	libretro-core = %{EVRD}

%description vba-next
VBA Next core for libretro. It's used to run Game Boy Advance games.

VBA Next is an optimized port of VBA-M to libretro.

%files vba-next
%{_libdir}/%{name}/vba_next_libretro.so

#----------------------------------------------------------------------------

%prep
%setup -q
# Drop usless cores
rm -rf libretro-gl-modelviewer
rm -rf libretro-gl-scenewalker
# virtual memory exhausted during build
rm -rf libretro-picodrive
# not ready yet
rm -rf libretro-mame078

%build
./libretro-build.sh

%install
mkdir -p %{buildroot}%{_libdir}/%{name}
./libretro-install.sh %{buildroot}%{_libdir}/%{name}

