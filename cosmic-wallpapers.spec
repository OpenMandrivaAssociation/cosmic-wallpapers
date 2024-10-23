%undefine _debugsource_packages

Name:           cosmic-wallpapers
Version:        1.0.0
Release:        0.alpha.2.1
Group:          Wallpapers/COSMIC
Summary:        Wallpapers for the COSMIC Desktop Environment
License:        CC-BY-4.0 OR  CC0-1.0
URL:            https://github.com/pop-os/cosmic-wallpapers
Source0:        https://github.com/pop-os/cosmic-screenshot/archive/epoch-%{version}-alpha.2/%{name}-epoch-%{version}-alpha.2.tar.gz
BuildRequires:  make

%description
%{summary}.

%prep
%autosetup -n %{name}-epoch-%{version}-alpha.2 -p1

%build
# nothing to build

%install
%make_install prefix=%{_prefix}

%files
%doc README.md
%dir %{_datadir}/backgrounds
%{_datadir}/backgrounds/cosmic
