Name:          bot_telegram                                  
Version:       1.1.1                                                                                                                                         
Release:       1%{?dist}                                                                                                                                                                      
Summary:       Bot telegram for Fedora 37                                                                      
                                                                                                                       
Group:          Miscellaneous                                                                                          
License:        Open Source                                                                                    
Source0:        %{name}-%{version}.tar.gz                                                                                                                                                                                                     
                                                                                                                       
Requires:       python                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                              
BuildArch:      x86_64                                                                                                                                                                        
                                                                                                                                                                                              
%description                                                                                                                                                                                  
Fedora package for Fedora                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                              
%prep                                                                                                                                                                                                                                                                                                                        
%setup -q                                                                                                                                                     
                                                                               
#%build                                                                                                                                                                                                                                                                                                                      
                                                                                               
#%pre                                                                                                                                                                                          
getent group usr_srvc_bot >/dev/null || groupadd -f -g 666 -r usr_srvc_bot                                                                                                                                  
if ! getent passwd usr_srvc_bot >/dev/null ; then                                                                                                                                                    
    if ! getent passwd 666 >/dev/null ; then                                                                                                                                                  
      useradd -r -u 666 -g usr_srvc_bot -d /var/lib/fedora_bot -s /sbin/nologin -c "Bot user account" usr_srvc_bot                                                                                                                                                                                                                                                                                            
    else                                                                                                                                                                                                                                                                                                                                                                                     
      useradd -r -g usr_srvc_bot -d /var/lib/fedora_bot -s /sbin/nologin -c "Bot user accoun" usr_srvc_bot                                                                                                                                                                                                                                                                                                    
    fi                                                                                         
    mkdir -p /var/lib/fedora_bot                                                                    
    chown usr_srvc_bot:usr_srvc_bot /var/lib/fedora_bot                                                           
    chmod 744 /var/lib/fedora_bot                                                                                           
fi                                                                                                                     
                                                                                                                       
%install                                                                                                               
rm -rf $RPM_BUILD_ROOT                                                                                                                                                                                                                        
#make install DESTDIR=$RPM_BUILD_ROOT                                                                                  
install -d -m 0755 %{buildroot}/etc/fedora_bot                                                                                                                                                install -d -m 0755 %{buildroot}/opt/fedora_bot
install -d -m 0755 %{buildroot}/var/log/fedora_bot  
install -d -m 0755 %{buildroot}/usr/lib/systemd/system/  
install -d -m 0755 %{buildroot}/etc/logrotate.d  
install -m 755 bot.py %{buildroot}/opt/fedora_bot/bot.py
install -m 755 bot.ini %{buildroot}/etc/fedora_bot/bot.ini
install -m 755 bot-telegram.service %{buildroot}/usr/lib/systemd/system/bot-telegram.service 
install -m 755 bot %{buildroot}/etc/logrotate.d/bot 
#cp -pR  bot-telegram.service %{buildroot}/usr/lib/systemd/system/bot-telegram.service 
cp -pR  bot_fedora_dependencies   %{buildroot}/opt/fedora_bot/
#chown usr_srvc_bot:usr_srvc_bot -R %{buildroot}/*                                                                                    



%files                                                                                                                 
/etc/fedora_bot                                                                                                        
/opt/fedora_bot     
/etc/logrotate.d                                                                                               
/var/log/fedora_bot                                                                                                        
/etc/logrotate.d/bot
/opt/fedora_bot/bot.py                                                                                              
/etc/fedora_bot/bot.ini                                                                                                   
/usr/lib/systemd/system/bot-telegram.service                                                                                                 
/opt/fedora_bot/bot_fedora_dependencies 
#/debugsourcefiles.list

%post                                                                                                                  
chown usr_srvc_bot:usr_srvc_bot -R /etc/fedora_bot                                                                                  
chown usr_srvc_bot:usr_srvc_bot -R /opt/fedora_bot 
chown usr_srvc_bot:usr_srvc_bot -R /var/log/fedora_bot
chown root:root /usr/lib/systemd/system/bot-telegram.service 




%changelog                                                                                                             
*   Mon Dec 19 2022 Juan Pablo Hernandez Castillo <papablo31@gmail.com>
    - Bot rpm   
