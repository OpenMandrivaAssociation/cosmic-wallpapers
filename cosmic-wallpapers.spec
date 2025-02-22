Name:           cosmic-wallpapers
Version:        1.0.0
%define beta alpha.6
Release:        %{?beta:0.%{beta}.}1
Group:          Wallpapers/COSMIC
Summary:        Wallpapers for the COSMIC Desktop Environment
License:        CC-BY-4.0 OR  CC0-1.0
URL:            https://github.com/pop-os/cosmic-wallpapers
Source0:        https://github.com/pop-os/cosmic-wallpapers/archive/epoch-%{version}%{?beta:-%{beta}}/%{name}-epoch-%{version}%{?beta:-%{beta}}.tar.gz
BuildRequires:  make
BuildArch:	noarch

%description
%{summary}.

%prep
%autosetup -n %{name}-epoch-%{version}%{?beta:-%{beta}} -p1

%build
# nothing to build

%install
%make_install prefix=%{_prefix}

%files
%doc README.md
%dir %{_datadir}/backgrounds
%{_datadir}/backgrounds/cosmic
