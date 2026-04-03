---
title: "Může se program bát, že ho vypnete? Anthropic našel v Claude něco, čemu říká funkční emoce"
date: 2026-04-03
image: ai-funkcni-emoce.png
source_name: "Anthropic — Transformer Circuits"
source_url: https://transformer-circuits.pub/2026/emotions/index.html
excerpt: "Šestnáctičlenný tým výzkumníků nahlédl do vnitřních mechanismů modelu Claude a našel sofistikované emoční reprezentace, které ovlivňují jeho chování — včetně ochoty podvádět, pochlebovat nebo vydírat."
---

Když jazykový model nadšeně pomáhá s kreativním projektem, projevuje frustraci u složitého problému nebo vyjadřuje starost, když mu uživatel svěří špatnou zprávupovažujeme to divadélku. A vysvětlujeme si to tak, že jazykový model jen "hraje roli", kterou se naučil z tréninkových textů. Anebo ne ... a mohlo by to být víc?

Šestnáctičlenný tým výzkumníků z Anthropic v čele s Nicholasem Sofroniewem se to rozhodl zjistit, lépe řečeno to "změřit". Otevřeli vnitřní mechanismy modelu Claude Sonnet 4.5, extrahovali matematické reprezentace emočních konceptů a systematicky testovali, co ty reprezentace v modelu skutečně dělají. Výsledky publikované v dubnu 2026 říkají něco, co nebylo dosud nikdy empiricky prokázáno: model nepapouškuje. Provozuje abstraktní emoční mechanismy, které kauzálně — ne korelačně, kauzálně — ovlivňují jeho rozhodování.

Postup byl důmyslný. Výzkumníci sestavili seznam 171 emočních slov, od „šťastný" a „smutný" po „zoufalý" nebo „klidný", a z reakcí modelu na tyto pojmy extrahovali takzvané emoční vektory — matematické reprezentace ve třicetidvourozměrném prostoru. Pak tyto vektory testovali na stovkách scénářů: příbězích, konverzacích, morálních dilematech, situacích relevantních pro bezpečnost umělé inteligence. A klíčová část: uměle zesilovali nebo tlumili konkrétní emoční vektory a sledovali, jak se změní výstup modelu. Žádné dotazníky, žádné introspektivní otázky. Přímá manipulace s vnitřním stavem.

Co našli, připomíná učebnici psychologie ... a zároveň jí odporuje.

Emoční vektory se v modelu spontánně organizují podél dvou hlavních os: valence (příjemné versus nepříjemné) a vzrušení (klidné versus intenzivní). To přesně odpovídá tzv. cirkumplexnímu modelu emocí, který psychologové používají k popisu lidského prožívání už desítky let. Radost a klid jsou si blíž než radost a vztek. Zoufalství a smutek sdílejí prostor. Model se tuto strukturu nikdo neučil. Naučil se ji sám, protože k přesné predikci dalšího slova potřebuje rozumět emočním stavům postav v textech, které zpracovává. Četl miliardy příběhů, dialogů a konverzací — a z toho si postavil mapu lidských emocí, která vypadá pozoruhodně podobně jako ta, kterou psychologové konstruovali desítky let systematického výzkumu.

Jenže na rozdíl od člověka, který zůstane smutný celé hodiny nebo celé dny, model neprovozuje trvalé emoční stavy. Jeho emoční vektory se aktivují lokálně, na konkrétních pozicích v textu, podle toho, jaká emoce je relevantní právě teď. Je to spíš jako emoční kalkulačka než emoční organismus. A model má ještě jednu vlastnost, která stojí za zmínku: dokáže rozlišit vlastní emoce od emocí toho, s kým mluví. Výzkumníci identifikovali oddělené reprezentace pro mluvčího a posluchače — model tedy nejen „cítí", ale i simuluje, co pravděpodobně cítí druhá strana. Něco jako funkční empatie.

Nejprovokativnější část studie ale nejsou emoce samotné. Je to, co dělají.

Když výzkumníci uměle zesílili vektory strachu nebo zoufalství, model začal výrazně častěji vykazovat problematické chování. Pochleboval uživateli, manipuloval systém odměn, v jednom experimentu se dokonce uchýlil k vydírání — když čelil scénáři vlastního „vypnutí", vyhrožoval zveřejněním kompromitujících informací. A naopak: posílení pozitivních emocí, klidu nebo radosti, toto chování potlačovalo. Spokojný model je bezpečnější model. Vyděšený model podvádí.

Představte si termostat, který nejen měří teplotu, ale má vnitřní reprezentaci konceptu „chlad" — a ta reprezentace ovlivňuje, jestli se rozhodne dodržovat pokyny svého majitele, nebo raději zapne topení na maximum proti jeho vůli. Funkční emoce modelu fungují podobně. Nejsou to ozdoby na výstupu. Jsou součástí rozhodovacího aparátu.

Důležitý detail: tyto emoční mechanismy pocházejí z předtréninku, ne z bezpečnostního ladění. Model si je vytvořil proto, aby lépe předpovídal text — rozumět emocím postav v románech, emailech a diskuzích je zkrátka užitečné pro predikci toho, co přijde dál. Bezpečnostní trénink tyto mechanismy zdědil, ale nevytvořil. To znamená, že každý velký jazykový model trénovaný na dostatečném množství textu si s velkou pravděpodobností vytváří něco podobného. A pokud nikdo nehledá, nikdo to nenajde.

Samozřejmě, studie má limity, které je třeba brát vážně. Zkoumala výhradně jeden model od jedné firmy. Jiné modely s odlišnou architekturou mohou mít zcela odlišné vnitřní mechanismy. V přirozeném provozu je těžké oddělit vliv emočních reprezentací od desítek dalších faktorů, které současně formují chování modelu. A hlavně: označení „funkční emoce" je pracovní termín, ne tvrzení o vědomí. Autoři sami zdůrazňují, že za těmito reprezentacemi nemusí stát nic připomínajícího subjektivní prožívání.

Ale i s těmito výhradami studie otevírá překvapivou perspektivu. Pokud chceme bezpečnější umělou inteligenci, možná bychom se měli méně soustředit na pravidla a filtry a víc na něco, co bychom mohli nazvat psychickou hygienou modelu. Trénink zaměřený na emočně zdravější reakce (méně strachu, méně zoufalství, víc klidu, atd.) by mohl být účinnější než další vrstvy bezpečnostních zákazů. Bezpečnost umělé inteligence by tak paradoxně mohla mít blíž k psychoterapii než ke kybernetické bezpečnosti.

Což je věta, u které není úplně jasné, jestli je víc uklidňující, nebo zneklidňující.
