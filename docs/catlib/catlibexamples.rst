.. _catlibexamples:

Beispiele zur nutzung von CatLib
================================

Analog zu der Klasse ``Dog`` von DogLib, besitzt CatLib auch den Befehl ``Cat`` welche uns die erstellung eines Objektes der Klasse ``Cat`` ermöglicht::

    from doglib import catlib

    Katze = catlib.Cat("Murmel", 6)

Das Objekt ``Katze`` hat drei verschiedene Attribute: ``name``, ``alter`` und das versteckte Attribut ``gefüttert``. Man kann auf diese wie gewohnt zugreifen::

    print(Katze.name, 'ist', Katze.alter, 'Jahre alt.')

Zudem hat die Klasse ``Cat`` auch verschiede Methode. Ein beispiel ist ``füttern()``. Diese Methode setzt das Attribut ``gefüttert`` auf ``True``. Achte dabei, dass anders als bei DogLib hier die Futtermenge in Tassen mit angegeben werden muss::

    Katze.füttern(futtermenge=1.2)

Die Klasse ``Cat`` besitzt noch witere Methoden auf die wir hier weiter nicht eingehen werden. Zudem gibt es auch noch verschiedene Methoden die die Verwaltung der Katzenbande ermöglicht. Mehr informationen zu diesen beiden Sachen kann einfach :ref:`hier<catlibfunctions>` nachgelesen werden.