---
title: "AI se nezlepšila. Přiznala si, že na to sama nestačí — a to byl průlom"
date: 2026-04-20
image: ai-pokora-ilustrace.png
source_name: The Wall Street Journal
source_url: https://www.wsj.com
excerpt: "Proč systémy, které halucinují ze své podstaty, jsou najednou dost spolehlivé na reálnou práci? Odpověď není v tom, že by AI zchytřela."
---

# AI se nezlepšila. Přiznala si, že na to sama nestačí — a to byl průlom

Začátkem dubna unikl na internet zdrojový kód Claude Code, jednoho z nejpoužívanějších AI nástrojů v Silicon Valley. Šlo o nehodu, společnost Anthropic kód rychle stáhla, ale škoda byla hotová. Lépe řečeno k žádné škodě nedošlo, možná spíš naopak. Výzkumníci, kteří se do kódu podívali, se nedočkali žádné sci-fi superinteligence. Místo toho našli něco mnohem obyčejnějšího: systém plný skriptů, pravidel a záplat. Jeden kousek kódu třeba detekuje, jestli je uživatel vzteklý, a to tak, že prohledává jeho zprávy a hledá nadávky.

Jenže právě v téhle banální všednosti se skrývá odpověď na otázku, která trápí každého, kdo s AI pracuje: proč systémy, které ze své podstaty halucinují a jsou nekonzistentní a nespolehlivé, jsou najednou dost dobré na to, aby se daly použít k reálné práci?

Odpověď není v tom, že by AI zchytřela. Je v tom, že se naučila přiznat, že na to sama nestačí.

*

Velké jazykové modely jsou ze své podstaty generátory pravděpodobnosti. Predikují, které slovo by mělo následovat po předchozím. To je elegantní, ale také hluboce nespolehlivé — model neví, co ví a co si jen vymýšlí. Halucinace, čili vymýšlení faktů s dokonale sebejistým výrazem, jsou jeho přirozeností, ne výjimkou.

Přesto se v posledních zhruba dvanácti měsících stalo něco, co zákazníci i skeptici začínají tiše přiznávat: ty věci fungují. Lépe než dřív. OpenAI tvrdí, že jeho nejnovější model dělá o 26 procent méně faktických chyb než GPT-4o. Google systematicky měří faktičnost svých modelů. Anthropic se drží výzkumu „kalibrace" — toho, aby model věděl, co neví, a přiznal to.

Tři věci se změnily. Žádná z nich není záhadná.

*

První je prosté vyhledávání. Dnes každý relevantní AI systém umí v případě potřeby zavolat Google nebo jiný vyhledávač a zkontrolovat, co je aktuálně na internetu. Vzniklo celé odvětví firem, které se specializují na to, že "stahují" z webů data a dodají je AI v přijatelném formátu. Z vnějšího pohledu je to přiznání porážky: model, který měl vědět vše, musí googlovat jako každý jiný. Ale jak jsme si řekl, LLMs fungují jinak a jejich síla je v něčem jiném. Googlování funguje.

Vedle toho roste průmysl kolem expertních dat — tisíce lidí, odborníků na medicínu, právo nebo finance, jsou placeni od hodiny za to, že zapisují své znalosti do trénovacích datasetů. AI se stala velmi drahým žákem, který potřebuje prémiové učitele, aby se neučil zbytečně špatně.

Druhá věc je matematika. Dříve jazykový model halucinoval i při sčítání. Teď, když dostane úlohu vyžadující výpočet, ji přesměruje na tradiční software — kód, kalkulačku, Python interpreter. Nebojuje s aritmetikou přes pravděpodobnost. Přizná si limit a předá štafetu nástroji, který je na to stavěný.

„LLM samotné jsou víceméně stejně nespolehlivé jako vždy," říká Gary Marcus, AI výzkumník a jeden z nejhlasitějších kritiků přehnaných očekávání od jazykových modelů. „Ale zejména v matematice a kódování dokážete výstup LLM předat dalším technologiím, které ho změní ve velmi užitečný."

Třetí věc je sebekontrola. Moderní AI systémy před odpovědí vedou samy se sebou cosi  jako vnitřní monolog — v oboru se tomu říká „chain of thought" — a procházejí daný problém, kontrolují učiněné kroky, snaží se chytit vlastní chyby. A v kritičtějších nasazeních přibývá praxe tzv. "radících" modelů: výstup jednoho AI zkontroluje jiný model, klidně od jiného výrobce. ChatGPT zkontroluje Claude, nebo naopak. Odpověď se akceptuje jen při shodě.

*

Leaknutý kód Claude Code ukazuje, jak výsledná architektura ve skutečnosti vypadá: je to komplikovaný sendvič, kde staré dobré softwarové inženýrství obaluje jazykový model. Skript na detekci vzteku. Systém správy paměti, aby kontext konverzace nezahltil model a nezačal zesilovat halucinace. Sada nástrojů, na které model volá, když narazí na to, co neumí.

Něco jako pokora zabudovaná do systému.

A tady je ta pointa, která se v nadšení kolem AI ztrácí: průlom nepřišel v momentě, kdy modely zchytřely. Přišel v momentě, kdy jejich tvůrci přestali věřit, že zchytří dost. Místo aby čekali na model, který bude vědět vše, postavili model, který umí přiznat, že neví. Nebo ještě lépe, ty modely musely nejdřív zjistit, že něco neví. A pak už jen povolat na pomoc někoho schopnějšího.

AI nenapodobila lidský mozek. Napodobila lidské instituce: encyklopedii, kalkulačku, recenzní řízení. Systém, ve kterém nikdo nemusí vědět vše, protože úkoly jsou rozděleny mezi specializované nástroje s jasnými kompetencemi.

V oboru, který roky sliboval umělou superinteligenci, se ukázalo, že nejužitečnější pokrok přineslo staré a ne zrovna vzrušující inženýrské řemeslo. Uvědomit si, co systém neumí. A postavit kolem toho podporu.
