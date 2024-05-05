.. _doglibfunctions:

Funktionen und Klassen
======================

Klassen
-------

.. class:: Dog(name, alter, größe)

   Initialisiert eine neue Instanz der Klasse Dog.

   :param str name: Der Name des Hundes.
   :param int alter: Das Alter des Hundes.
   :param str oder int größe: Die Größe des Hundes.
   :raises TypeError: Wenn einer der Eingabeparameter nicht den erwarteten Typ hat.

   .. method:: bellen()

      Lässt den Hund bellen und gibt dabei seinen Namen aus.

   .. method:: spielen()

      Lässt den Hund spielen und gibt eine entsprechende Ausgabe aus.

   .. method:: füttern()

      Füttert den Hund und markiert ihn als gefüttert.

   .. method:: umbenennen(neuer_name)

      Benennt den Hund um.

      :param str neuer_name: Der neue Name des Hundes.
      :raises TypeError: Wenn der Eingabeparameter nicht den erwarteten Typ hat.

   .. method:: wach()

      Überprüft, ob der Hund wach ist.

      :returns: True, wenn der Hund wach ist, False sonst.
      :rtype: bool

   .. method:: alter_in_menschenjahren()

      Berechnet das Alter des Hundes in Menschenjahren.

      :returns: Das Alter des Hundes in Menschenjahren.
      :rtype: int

Funktionen
----------

.. function:: umrechnung_futtergewicht_in_tassen(futtergewicht)

   Rechnet das Futtergewicht in Tassen um.

   :param float futtergewicht: Das Gewicht des Futters in Gramm.
   :returns: Das Futtergewicht in Tassen.
   :rtype: float

.. function:: alle_hunde()

   Gibt eine Liste aller existierenden Hunde zurück.

   :returns: Eine Liste aller existierenden Hunde.
   :rtype: list

.. function:: alle_hunde_listen()

   Gibt die Namen aller existierenden Hunde aus.

.. function:: alle_hungrigen_hunde_listen()

   Gibt die Namen aller hungrigen Hunde aus.