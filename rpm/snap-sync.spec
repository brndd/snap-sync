Name:           snap-sync
Version:        0.7
Release:        1%{?dist}
Summary:        Use snapper snapshots to backup to external drive

License:        GPLv2
URL:            https://github.com/wesbarnett/snap-sync/
Source0:        https://github.com/wesbarnett/snap-sync/releases/download/%{version}/%{name}-%{version}.tar.gz

Requires:       bash, snapper, btrfs-progs, gawk, util-linux, sed, openssh-clients
BuildArch:      noarch

%description
This bash script sends incremental snapshots to
another drive for backing up data.

%prep
%autosetup -n %{name}


%build


%install
rm -rf $RPM_BUILD_ROOT
%make_install SNAPPER_CONFIG=/etc/sysconfig/snapper

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
* Sun January 24 2021 Pekka Oinas <peoinas@gmail.com> 0.7-1
- Update to version 0.7

* Fri Aug 28 2020 peoinas <peoinas@gmail.com> 0.6.1-1
- Packaging version 0.6.1
