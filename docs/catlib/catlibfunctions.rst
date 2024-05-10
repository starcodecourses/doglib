.. _catlibfunctions:

Funktionen und Klassen in CatLib
================================

Cat
---

.. class:: Cat(name, alter)

   Initialisiert eine neue Instanz der Klasse Cat.

   :param str name: Der Name der Katze.
   :param int alter: Das Alter der Katze.
   :raises TypeError: Wenn einer der Eingabeparameter nicht den erwarteten Typ hat.

   .. method:: miezen()

      Gibt den Miau-Laut der Katze mit dem entsprechenden Namen aus.

   .. method:: spielen()

      Spielt mit der Katze.

   .. method:: füttern(futtermenge=1.2)

      Füttert die Katze.

      :param float futtermenge: Die Menge an Futter, die der Katze gegeben wird. Standardwert ist 1.2.

   .. method:: umbenennen(neuer_name)

      Benennt die Katze um.

      :param str neuer_name: Der neue Name der Katze.
      :raises TypeError: Wenn der Eingabeparameter nicht den erwarteten Typ hat.

   .. method:: wach()

      Überprüft, ob die Katze wach ist.

      :returns: True, wenn die Katze wach ist, False sonst.
      :rtype: bool

   .. method:: alter_in_menschenjahren()

      Berechnet das Alter der Katze in Menschenjahren.

      :returns: Das Alter der Katze in Menschenjahren.
      :rtype: int

Funktionen
----------

.. function:: umrechnung_futtergewicht_in_tassen(futtergewicht)
   :no-index:

   Rechnet das Futtergewicht in Tassen um.

   :param float futtergewicht: Das Gewicht des Futters in Gramm.
   :returns: Die Anzahl der Tassen, die dem Futtergewicht entsprechen.
   :rtype: float

.. function:: alle_katzen()

   Gibt eine Liste aller Katzen-Objekte zurück.

   :returns: Eine Liste aller Katzen-Objekte.
   :rtype: list

.. function:: alle_katzen_listen()

   Gibt die Namen aller Katzen aus.

.. function:: alle_hungrigen_katzen_listen()

   Gibt eine Liste aller hungrigen Katzen-Objekte zurück.

   :returns: Eine Liste aller hungrigen Katzen-Objekte.
   :rtype: list