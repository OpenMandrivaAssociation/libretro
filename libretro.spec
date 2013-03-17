# Debug depends on system CFLAGS but various cores use their own
# It's quite a pain to patch every core for CFLAGS and maintain patches
# And debug is not really needed here anyway
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Name:		libretro
Version:	20130317
Release:	1
Summary:	An interface for emulator and game ports
Group:		Emulators
# Actually, various for each core but mostly GPLv2
License:	GPL
URL:		http://www.libretro.org/
# fetched via libretro-fetch.sh from git and re-packed
Source:		%{name}-%{version}.tar.bz2
Suggests:	retroarch

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

%prep
%setup -q

%build
./libretro-build.sh

%install
./libretro-install.sh %{buildroot}%{_libdir}/%{name}

%files
%{_libdir}/%{name}/libretro-bnes.so
%{_libdir}/%{name}/libretro-bsnes-accuracy.so
%{_libdir}/%{name}/libretro-bsnes-balanced.so
%{_libdir}/%{name}/libretro-bsnes-performance.so
%{_libdir}/%{name}/libretro-desmume.so
%{_libdir}/%{name}/libretro-fba.so
%{_libdir}/%{name}/libretro-fceu.so
%{_libdir}/%{name}/libretro-gambatte.so
%{_libdir}/%{name}/libretro-genplus.so
%{_libdir}/%{name}/libretro-mednafen-psx.so
%{_libdir}/%{name}/libretro-meteor.so
%{_libdir}/%{name}/libretro-nestopia.so
%{_libdir}/%{name}/libretro-nx.so
%{_libdir}/%{name}/libretro-prboom.so
%{_libdir}/%{name}/libretro-quicknes.so
%{_libdir}/%{name}/libretro-snes9x-next.so
%{_libdir}/%{name}/libretro-snes9x.so
%{_libdir}/%{name}/libretro-stella.so
%{_libdir}/%{name}/libretro-tyrquake.so
%{_libdir}/%{name}/libretro-vba.so
