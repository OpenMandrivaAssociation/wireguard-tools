%global debug_package %{nil}
%define shapshot 20200319

Summary:	Fast, modern, secure VPN tunnel
Name:		wireguard-tools
URL:		https://www.wireguard.com/
Version:	1.0.2020319
Release:	1
License:	GPLv2
Group:		Networking/Other
Source0:	https://git.zx2c4.com/%{name}/snapshot/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(libmnl)
Requires:	kmod(wireguard.ko)

%description
WireGuard is a novel VPN that runs inside the Linux Kernel and uses
state-of-the-art cryptography (the "Noise" protocol). It aims to be
faster, simpler, leaner, and more useful than IPSec, while avoiding
the massive headache. It intends to be considerably more performant
than OpenVPN. WireGuard is designed as a general purpose VPN for
running on embedded interfaces and super computers alike, fit for
many different circumstances. It runs over UDP.

This package provides the wg binary for controling WireGuard.

%prep
%autosetup -p1

%build
cd %{_builddir}/%{name}-%{version}/src
%make_build

%install
cd %{_builddir}/%{name}-%{version}/src
%make_install WITH_BASHCOMPLETION=yes WITH WGQUICK=yes WITH_SYSTEMDUNITS=yes

%files
%doc README.md
%{_bindir}/wg
%{_bindir}/wg-quick
%{_datadir}/bash-completion/completions/wg
%{_datadir}/bash-completion/completions/wg-quick
%{_unitdir}/wg-quick@.service
%{_mandir}/man8/wg.8*
%{_mandir}/man8/wg-quick.8*
