.. _installation:

Installation
============

.. contents::
    :local:
    :depth: 1

Es gibt zwei Arten DogLib zu installieren. Entweder über ``pip`` oder über ``conda``. Wie ihr im Python-Grundlagenkurs gelernt habt, ist ``pip`` ein Paket manager für Python, der es einfach macht, Python-Pakete zu installieren, zu aktualisieren und zu deinstallieren. ``conda`` ist ein weiterer Paketmanager, der speziell für die Verwaltung von Datenwissenschaftspaketen entwickelt wurde. Für den Anfang empfehlen wir die Installation über ``pip`` da es die einfachste und schnellste Methode ist! Natürlich hängt das aber auch davon ab, was ihr bereits installiert habt.

.. note::
    Zu der Installation dieses Pakets wird mindestens Python 3.6 benötigt. Wenn ihr eine ältere Version von Python habt, müsst ihr diese zuerst aktualisieren. Zudem wird die Python-Bibliothek ``numpy`` benötigt (siehe `NumPy <https://numpy.org/>`_). Diese wird automatisch installiert, wenn ihr ``doglib`` installiert.

Installationsmethoden
---------------------

.. tabs::
    .. group-tab:: PyPI Paket (``pip``)  
       DogLib ist im PyPI-Paketindex enthalten: https://pypi.python.org/pypi/doglib
        Du kannst daher DogLib mit dem ``pip``-Paketmanager installieren. Gebe dazu den foldenden Befehl in deinem Terminal biehungsweise in deiner Kommandozeile ein::
    
            python -m pip install doglib

        Sollte ein Fehler auftreten, dann frage gerne einen deine Lehrenden, oder schreibe uns eine E-Mail!

    .. group-tab:: Anaconda Paket (``conda``)  
       DogLib ist auch im conda-Paketindex enthalten: https://anaconda.org/starcode/doglib
        Du kannst daher DogLib mit dem ``conda``-Paketmanager installieren. Gebe dazu den foldenden Befehl in deinem Terminal biehungsweise in deiner Kommandozeile ein::
    
            conda install starcode::doglib 
        
        Hier ist es zudem noch notwendig, das Paket `NumPy <https://numpy.org/>`_ zu installieren, da DogLib dieses benötigt::
                
            conda install numpy
        
        Nun solltest du DogLib nutzen können! Sollte ein Fehler auftreten, dann frage gerne einen deine Lehrenden, oder schreibe uns eine E-Mail!