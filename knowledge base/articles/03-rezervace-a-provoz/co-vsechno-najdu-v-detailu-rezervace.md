# Co všechno najdu v detailu rezervace

## Co tento článek řeší

Ukazuje detail rezervace jako pracovní místo pro jeden konkrétní pobyt: kde ověřit data, co poslat hostovi, jak poznat stav registrace, kde upravit hosty a kdy řešit Ubyport nebo e-maily.

## Pro koho je článek určen

- pro hostitele, kteří řeší jeden konkrétní pobyt
- pro uživatele, kteří potřebují rychle ověřit data rezervace

## Kdy detail rezervace otevřít

Detail otevřete ve chvíli, kdy řešíte jeden konkrétní pobyt. Typicky když:

- chcete ověřit, jestli rezervace sedí na správnou nemovitost a termín
- potřebujete doplnit jméno hosta, počet hostů, jazyk nebo cenu
- chcete poslat hostovi registrační odkaz nebo zkontrolovat text zprávy
- kontrolujete, jestli hosté vyplnili formulář pro domovní knihu
- potřebujete vidět, jaké e-maily systém k rezervaci odeslal
- řešíte hlášení zahraničních hostů přes Ubyport
- chcete vystavit fakturu nebo zkontrolovat cenu rezervace

## Co zkontrolovat hned nahoře

V horní části detailu najdete rychlý souhrn rezervace: hosta, termín příjezdu a odjezdu, relativní informaci k příjezdu a název nemovitosti. Vedle toho je akce pro synchronizaci zdroje rezervace.

Tahle část je dobrá pro první kontrolu:

1. ověřte hosta a nemovitost
2. zkontrolujte datum příjezdu a odjezdu
3. podívejte se, jestli rezervace není zrušená
4. pokud data nesedí, použijte synchronizaci zdroje

Pokud systém zjistí, že chybí údaje v profilu nebo u nemovitosti, zobrazí nad obsahem upozornění. Typicky jde o data potřebná pro reporty, exporty nebo navazující administrativu.

## Jak číst workflow rezervace

Workflow nahoře ukazuje, v jaké fázi rezervace je a kdo má udělat další krok.

- `Import rezervace` znamená, že rezervace už existuje v systému
- `Příprava zprávy pro hosta` je krok hostitele, kdy kopírujete nebo upravujete zprávu s odkazem
- `Registrace hosta` znamená, že host vyplňuje nebo už vyplnil formulář
- `Hlášení cizinecké policii` se zobrazí hlavně u zahraničních hostů
- `Dokončeno` znamená, že pro rezervaci není potřeba další běžná akce

Nejdůležitější je nečíst workflow jako dekoraci. Je to rychlá odpověď na otázku: `Co mám s touhle rezervací udělat teď?`

## Přehled: host, termín, cena a zdroj

V záložce `Přehled` jsou dvě hlavní karty.

V části `Informace o hostovi` můžete kontrolovat nebo upravit:

- jméno hosta
- e-mail a telefon, pokud jsou k dispozici
- počet hostů
- jazyk hosta pro zprávu a formuláře

Počet hostů je důležitý. Pokud je nastavený na `0`, systém vás upozorní, protože bez správného počtu hostů nedává smysl posílat registrační odkazy ani čekat kompletní domovní knihu.

V části `Detaily rezervace` kontrolujete:

- datum a čas příjezdu
- datum a čas odjezdu
- zdroj rezervace, například Airbnb, Booking.com nebo ruční zadání
- odkaz na rezervaci na původní platformě, pokud existuje
- celkovou cenu rezervace

Cenu lze upravit přímo v detailu. To se hodí hlavně tam, kde iCal přinesl termín, ale finanční data přišla později z email forwardingu nebo je potřebujete doplnit ručně.

## Zpráva pro hosta a registrační odkazy

Když rezervace čeká na údaje od hosta, detail zobrazí další kroky. V této části řešíte zprávu, kterou hostovi pošlete.

Najdete zde:

- náhled zprávy pro hosta
- tlačítko pro zkopírování zprávy
- možnost upravit text zprávy pro konkrétní rezervaci
- odkaz pro potvrzení rezervace
- po potvrzení také registrační formulář pro hosty

Rozdíl mezi odkazy:

- odkaz pro potvrzení rezervace pomáhá hostovi potvrdit rezervaci a dostat se k dalšímu kroku
- registrační formulář slouží pro vyplnění údajů hostů do domovní knihy
- permalink pro nemovitost se hodí do automatizovaných zpráv na Airbnb, aby hosté našli své rezervace pro danou nemovitost

Pokud máte pro nemovitost nastavené automatizované šablony zpráv, detail umí ukázat i jejich náhled pro jazyk vybraný u rezervace.

Šablony zpráv nemusíte používat jen ve výchozí podobě. U nemovitosti si můžete připravit vlastní texty zpráv a v detailu rezervace pak zkontrolovat, jak se do nich doplní konkrétní host, termín, cena nebo registrační odkaz.

> **Chcete zprávy posílat automaticky?**
>
> Pokud nechcete zprávu kopírovat ručně u každé rezervace, nastavte si automatizaci zpráv pro celou nemovitost. Šablona pak může hostovi automaticky poslat správný odkaz i instrukce podle konkrétní rezervace.
>
> Pokračujte článkem `Jak fungují automatizace v Superhostem`.

## Registrovaní hosté

Sekce `Registrovaní hosté` ukazuje, kolik formulářů je vyplněných a co u jednotlivých hostů chybí.

V tabulce najdete zejména:

- pořadí hosta v rezervaci
- jméno a e-mail
- datum narození
- adresu
- typ hosta, například dospělý, dítě nebo host bez poplatku
- národnost
- typ a číslo dokladu
- fotku čísla dokladu, pokud ji host nahrál
- stav vyplnění

U vyplněného hosta můžete otevřít formulář, zkopírovat odkaz, upravit údaje nebo hosta smazat. Pokud host ještě data nevyplnil, uvidíte stav `Čeká na vyplnění`.

## Ubyport a zahraniční hosté

Pokud jsou v rezervaci zahraniční hosté, detail může zobrazit akci pro Ubyport. Ta navazuje na data vyplněná ve formuláři hosta.

Před odesláním do Ubyport zkontrolujte hlavně:

- že počet hostů odpovídá realitě
- že zahraniční hosté mají vyplněnou národnost
- že nechybí datum narození
- že je doplněný typ a číslo dokladu
- že je správná adresa pobytu a údaje nemovitosti

Pokud některé z těchto údajů chybí, nejdřív opravte hosta nebo nastavení nemovitosti. Až potom dává smysl řešit export nebo odeslání.

## E-maily

Záložka `E-maily` ukazuje historii e-mailů odeslaných k rezervaci. Uvidíte:

- kdy byl e-mail odeslán
- komu byl odeslán
- předmět
- typ e-mailu, například pozvánka k registraci, odkaz pro úpravu nebo potvrzení
- stav, například odesláno, doručeno, selhalo nebo vráceno

Tahle záložka je užitečná ve chvíli, kdy host tvrdí, že nic nedostal, nebo když potřebujete ověřit, jestli systém zprávu opravdu odeslal.

## Rychlý postup při kontrole rezervace

1. Ověřte hosta, nemovitost a termín pobytu.
2. Zkontrolujte počet hostů a jazyk hosta.
3. Podívejte se na workflow a určete další krok.
4. Pokud host ještě nevyplnil údaje, zkopírujte zprávu nebo registrační odkaz.
5. Po vyplnění formulářů zkontrolujte tabulku registrovaných hostů.
6. U zahraničních hostů zkontrolujte data pro Ubyport.
7. Pokud host tvrdí, že zpráva nepřišla, otevřete záložku `E-maily`.
8. Pokud nesedí termín, cena nebo zdroj, zkontrolujte iCal a email forwarding.

## Co dělat, když něco nesedí

Když chybí termín nebo rezervace vůbec nevznikla, začněte u iCal napojení. Když chybí cena, částka nebo finanční detail, zkontrolujte email forwarding. Když chybí údaje hostů, pošlete nebo zkopírujte registrační odkaz z detailu rezervace.

Neřešte všechno najednou. Detail rezervace je nejlepší číst podle otázky, kterou právě řešíte:

- `Sedí pobyt?` kontrolujte termín, nemovitost a zdroj
- `Mám data hostů?` kontrolujte počet hostů a tabulku registrovaných hostů
- `Odešla komunikace?` kontrolujte zprávu a záložku e-maily
- `Můžu hlásit Ubyport?` kontrolujte zahraniční hosty a úplnost dokladů

## Doporučený další krok

Pokud v detailu chybí cena nebo finanční údaje, pokračujte článkem `Jak funguje email forwarding`. Pokud v detailu chybí samotná rezervace nebo termín, pokračujte článkem `Jak funguje napojení přes iCal`.
