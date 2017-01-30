Summary:	GUI for Yubikey personalization
Name:		yubikey-personalization-gui
Version:	3.1.24
Release:	1
License:	BSD
Group:		X11/Applications
URL:		http://opensource.yubico.com/yubikey-personalization-gui/
Source0:	http://opensource.yubico.com/yubikey-personalization-gui/releases/%{name}-%{version}.tar.gz
# Source0-md5:	79fcb86f6a95d945811746d5e52b6042
BuildRequires:	desktop-file-utils
BuildRequires:	libyubikey-devel >= 1.11
BuildRequires:	qt-devel
BuildRequires:	ykpers-devel >= 1.14.1

%description
Yubico's YubiKey can be re-programmed with a new AES key. This is a
graphical tool that makes this an easy task.

%prep
%setup -q

%build
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -D -p build/release/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D -p resources/lin/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

install -d $RPM_BUILD_ROOT/%{_pixmapsdir}
install -p resources/lin/%{name}.xpm $RPM_BUILD_ROOT/%{_pixmapsdir}/
install -p resources/lin/%{name}.png $RPM_BUILD_ROOT/%{_pixmapsdir}/

desktop-file-install --dir=$RPM_BUILD_ROOT%{_desktopdir} \
    resources/lin/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README COPYING ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
%{_pixmapsdir}/%{name}.png
%{_mandir}/man1/%{name}.1*
