.. _introduction:

Einführung
==========

.. contents::
    :local:
    :depth: 1

Die Python-Bibliothek ``doglib`` kann dir dabei helfen die einzelnen Hunde in einem großen Rudel zu verwalten. Du kannst Hunde hinzufügen, entfernen und Informationen über sie abrufen. Dazu musst du lediglich die Klasse ``Dog`` importieren und ein Objekt dieser Klasse erstellen.

Hier ist ein Beispiel, wie du die Bibliothek verwenden kannst::
    
        from doglib import Dog
    
        Hund = Dog("Rex", 5, "Groß")

Achte dabei drauf, dass du bei der erstellung eines Hundes immer den Namen, das Alter und die Größe angibst.

Das neu erstellte Objekt ``Hund`` enthält nun Informationen über den Hund. Auf diese kannst du zugreifen, indem du die Attribute des Objekts verwendest. Hier sind einige Beispiele::

        print(Hund.name)
        print(Hund.alter)
        print(Hund.größe)

Allerdings besitzt die Klasse ``Dog`` auch noch ein vestecktes Attribut das angibt ob der Hund schon gefüttert wurde oder nicht. Auf dieses attribut kannst du wie folgt zugreifen::

        print(Hund.gefüttert)

Es handelt sich dabei um ein Boolean-Attribut, das standardmäßig auf ``False`` gesetzt ist. Du kannst es auf ``True`` setzen, indem du die Methode ``füttern()`` aufrufst::

        Hund.füttern()
        print(Hund.gefüttert)

Neben der Klasse ``Dog`` enthält die Bibliothek aber auch noch verschiedene Funktionen, die dir dabei helfen können, die Hunde zu verwalten. So kannst du zum Beispiel alle erstellten Hunde anzeigen lassen in dem du die Funktion ``alle_hunde_listen()`` aufrufst::

        from doglib import alle_hunde_listen
    
        alle_hunde_listen()

Um eine geneauere übersicht über diese Funktionen und die Klasse ``Dog`` zu erhalten verweisen wir auf eine `genauere Beschreibung der einzelnen Funktionen <doglibfunction>`_ in dieser Dokumentation. Zudem enthält diese Bibliothek ein Modul welches dir helfen kann eine Katzenbande zu verwalten. Die Docuemtation dazu findest du `hier <_catlibintroduction>`_.