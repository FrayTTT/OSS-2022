Name:          505-5
Version:       1.0
Release:       1%{?dist}
Summary:       Программа студента Gorokhov Nikita группы B20-505
Group:         Testing
License:       GPL
URL:           https://github.com/FrayTTT/OSS-2022
Source0:       %{name}-%{version}.tar.gz
BuildRequires: /bin/rm, /bin/mkdir, /bin/cp
Requires:      /bin/bash, /usr/bin/date
BuildArch:     noarch

%description
A test package

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 505-5-1.0 %{buildroot}%{_bindir}
sudo yum install gnuplot

%files
%{_bindir}/505-5-1.0

%changelog
* Thu Oct 16 2012 Gorokhov
- Added %{_bindir}/505-5-1.0
