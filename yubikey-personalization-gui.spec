Summary:	GUI for Yubikey personalization
Summary(pl.UTF-8):	Graficzny interfejs użytkownika do personalizacji urządzeń Yubikey
Name:		yubikey-personalization-gui
Version:	3.1.25
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	https://developers.yubico.com/yubikey-personalization-gui/Releases/%{name}-%{version}.tar.gz
# Source0-md5:	33f4312281ada355c62f7232b57ad0b3
URL:		https://developers.yubico.com/yubikey-personalization-gui/
BuildRequires:	OpenGL-devel
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	desktop-file-utils
BuildRequires:	libyubikey-devel >= 1.11
BuildRequires:	qt5-build >= 5
BuildRequires:	qt5-qmake >= 5
BuildRequires:	ykpers-devel >= 1.14.1
Requires:	libyubikey >= 1.11
Requires:	ykpers >= 1.14.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yubico's YubiKey can be re-programmed with a new AES key. This is a
graphical tool that makes this an easy task.

%description -l pl.UTF-8
Urządzenia Yubico YubiKey można ponownie zaprogramować nowym kluczem
AES. To graficzne narzędzie pozwala zrobić to łatwo.

%prep
%setup -q

%build
qmake-qt5 \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}" \
	CONFIG+=nosilent
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -D -p build/release/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D -p resources/lin/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

install -d $RPM_BUILD_ROOT%{_pixmapsdir}
cp -p resources/lin/%{name}.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
cp -p resources/lin/%{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

desktop-file-install --dir=$RPM_BUILD_ROOT%{_desktopdir} \
	resources/lin/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
%{_pixmapsdir}/%{name}.png
%{_mandir}/man1/%{name}.1*
