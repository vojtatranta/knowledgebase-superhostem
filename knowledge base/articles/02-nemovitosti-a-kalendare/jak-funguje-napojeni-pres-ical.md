# Jak získat a napojit iCal z Airbnb a Bookingu

## Co tento článek řeší

Ukazuje, jak v aktuálním flow získat iCal z Airbnb nebo Booking.com, vložit ho do Superhostem a zkontrolovat, že se kalendář správně propsal.

## Pro koho je článek určen

- pro uživatele připojující Airbnb nebo Booking.com
- pro hostitele, kteří chtějí rozumět synchronizaci kalendářů

## Co iCal umí a co ne

iCal je formát kalendářových dat, přes který lze sdílet informace o rezervovaných a blokovaných termínech mezi různými systémy.

## Co iCal běžně přenáší

Přes iCal se typicky přenáší:

- datum začátku rezervace
- datum konce rezervace
- blokované termíny
- základní identifikace události

## Co iCal obvykle nepřenáší

iCal obvykle neobsahuje detailní finanční informace, například:

- cenu rezervace
- výši poplatků
- detailní rozpad provizí
- kompletní údaje o hostovi

Proto Superhostem kombinuje kalendářová data s dalšími zdroji, například s email forwardingem.

## Kdy iCal použít

iCal dává největší smysl na začátku, když chcete rychle propojit kalendář s nemovitostí a dostat do systému první rezervace nebo blokace termínů.

Pokud pak chcete pracovat i s detailnějšími údaji o rezervacích, navazuje na něj email forwarding a automatizace.

## Jak získat iCal z Airbnb

1. otevřete `Kalendář` na Airbnb
2. přejděte do části `Availability`
3. v bloku `Connect calendars` zvolte `Connect to another website`
4. zkopírujte celý iCal odkaz končící na `.ics`

## Jak získat iCal z Booking.com

1. přihlaste se do Extranetu Booking.com
2. otevřete `Calendar` nebo `Calendar & Pricing`
3. přejděte do `Sync calendars`
4. zvolte `Add calendar connection`
5. použijte `Copy link` a zkopírujte exportní odkaz pro správnou jednotku

## Jak vložit iCal do Superhostem

1. otevřete detail konkrétní nemovitosti
2. najděte část pro kalendáře nebo `iCal`
3. vložte zkopírovanou iCal URL
4. zdroj si srozumitelně pojmenujte, například `Airbnb` nebo `Booking`
5. uložte nastavení

## Jak poznat, že napojení funguje

- se zobrazují rezervované nebo blokované termíny
- data odpovídají zdrojové platformě
- změny se po čase propisují i do systému

## Na co si dát pozor

- zkopírujte vždy celý iCal odkaz, ne jen jeho část
- u více jednotek si hlídejte správnou vazbu mezi kalendářem a nemovitostí
- iCal nepřenáší ceny ani úplné finanční informace
- pokud se nic nepropsalo, zkontrolujte platnost odkazu a správnou jednotku

## Doporučený další krok

Pokud potřebujete vedle kalendářových dat i detailnější údaje o rezervacích, pokračujte článkem `Jak funguje email forwarding`.
