Name:       c-505-5
Version:    1.0
Release:    1%{?dist}
Summary:    Программа студента Gorokhov Nikita группы B20-505
Group:      Testing
License:    GPL
URL:        https://github.com/FrayTTT/OSS-2022
Source:     %{name}-%{version}.tar.gz
BuildRequires: gcc

%global debug_package %{nil}

%description
A test package

%prep
%setup -q

%build
gcc -O2 -o c-505-5 c-505-5.c

%install
mkdir -p %{buildroot}%{_bindir}
cp c-505-5 %{buildroot}%{_bindir}
sudo rpm -i ~/rpmbuild/RPMS/noarch/505-5-1.0-1.fc36.noarch.rpm --force

%files
%{_bindir}/c-505-5

%changelog
* Thu Oct 16 2012 Gorokhov
- Added %{_bindir}/c-505-5
