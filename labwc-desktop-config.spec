Name:       labwc-desktop-config
Version:    0.1
Release:    1
Summary:    Labwc desktop config for XFCE Wayland session and LXQT Wayland session
License:    GPL-2.0-only
URL:        https://github.com/OpenMandrivaAssociation/labwc-desktop-config
Source0:    LXQt-Wayland.tar.xz
Requires: labwc

%description
Labwc desktop config for XFCE Wayland session and LXQT Wayland session

%package desktop-LXQt-Wayland
Summary:	LXQt Wayland desktop configuration
Group:		Graphical desktop/LXQt
Suggests:	plasma6-breeze
Suggests:	kf6-breeze-icons
Suggests:	noto-sans-fonts

BuildArch:	noarch

%description desktop-LXQt-Wayland
LXQt-Wayland desktop configuration

%prep
%autosetup -n LXQt-Wayland -p1

%build
# nothing

%install

### DESKTOP LXQT-Wayland ###
mkdir -p %{buildroot}%{_sysconfdir}/xdg
cp -a * %{buildroot}%{_sysconfdir}/xdg
### DESKTOP LXQT-Wayland END ###

%files desktop-LXQt-Wayland
%{_sysconfdir}/xdg/featherpad
%{_sysconfdir}/xdg/gtk-3.0
%{_sysconfdir}/xdg/lxqt
%{_sysconfdir}/xdg/pcmanfm-qt
%{_sysconfdir}/xdg/qterminal.org
