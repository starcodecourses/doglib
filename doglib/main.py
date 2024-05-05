import gc
import numpy as np

class Dog:
  instances = []
  def __init__(self, name, alter, größe):
    """
    Initialisiert eine neue Instanz der Klasse Dog.

    Parameter:
      name (str): Der Name des Hundes.
      alter (int): Das Alter des Hundes.
      größe (str oder int): Die Größe des Hundes.

    Verursacht:
      TypeError: Wenn einer der Eingabeparameter nicht den erwarteten Typ hat.
    """
    self.__class__.instances.append(self)
    # Überprüft den Typ der Inputparameter
    if not isinstance(name, str):
      raise TypeError("`name` muss vom Typ 'string' sein")
    if not isinstance(alter, int):
      raise TypeError("`alter` muss vom Typ 'integer' sein")
    if not (isinstance(größe, str) or isinstance(größe, int)):
      raise TypeError("`größe` muss vom Typ 'string' oder 'integer' sein")
    self.name = name
    self.alter = alter
    self.größe = größe
    # Nicht benutzerinitiierte Atrribute
    self.gefüttert = False

  def bellen(self):
    """
    Lässt den Hund bellen und gibt dabei seinen Namen aus.
    """
    print(f"Woof! Ich heiße {self.name}.")

  def spielen(self):
    """
    Lässt den Hund spielen und gibt eine entsprechende Ausgabe aus.
    """
    if np.random.choice([True, False], p=[0.01, 0.99]):
      print(self.name, "rennt gegen die Wand. Autsch!")
    else:
      spielobjekt = np.random.choice(["einem Ball", "einem Knochen", "einem Stock", "einem Stofftier"])
      print(self.name, "spielt mit", spielobjekt, "und hat sichtlich Spaß.")

  def füttern(self):
    """
    Füttert den Hund und markiert ihn als gefüttert.
    """
    if self.gefüttert:
      print("Ich wurde bereits gefüttert!")
    else:
      self.gefüttert = True
      print("Woof! Ich bin nun satt.")

  def umbenennen(self, neuer_name):
    """
    Benennt den Hund um.

    Parameter:
      neuer_name (str): Der neue Name des Hundes.

    Verursacht:
      TypeError: Wenn der Eingabeparameter nicht den erwarteten Typ hat.
    """
    if not isinstance(neuer_name, str):
      raise TypeError("`neuer_name` muss vom Typ 'string' sein")
    self.name = neuer_name

  def wach(self):
    """
    Überprüft, ob der Hund wach ist.

    Rückgabe:
      bool: True, wenn der Hund wach ist, False sonst.
    """
    return np.random.choice([True, False], p=[12/24, 12/24])

  def alter_in_menschenjahren(self):
    """
    Berechnet das Alter des Hundes in Menschenjahren.

    Rückgabe:
      int: Das Alter des Hundes in Menschenjahren.
    """
    menschenalter = 16*np.log(self.alter) + 31
    return int(menschenalter)


def umrechnung_futtergewicht_in_tassen(futtergewicht):
  """
  Rechnet das Futtergewicht in Tassen um.

  Parameter:
    futtergewicht (float): Das Gewicht des Futters in Gramm.

  Rückgabe:
    float: Das Futtergewicht in Tassen.
  """
  tassen = futtergewicht/150    # 150g pro Tasse
  return tassen

def alle_hunde():
  """
  Gibt eine Liste aller existierenden Hunde zurück.

  Rückgabe:
    list: Eine Liste aller existierenden Hunde.
  """
  hunde = []
  for obj in gc.get_objects():
    if isinstance(obj, Dog):
      hunde.append(obj)
  return hunde

def alle_hunde_listen():
  """
  Gibt die Namen aller existierenden Hunde aus.
  """
  for obj in gc.get_objects():
    if isinstance(obj, Dog):
      print(obj.name)

def alle_hungrigen_hunde_listen():
  """
  Gibt die Namen aller hungrigen Hunde aus.
  """
  hungrige_hunde = []
  for obj in gc.get_objects():
    if isinstance(obj, Dog):
      if not obj.gefüttert:
        hungrige_hunde.append(obj)
  return hungrige_hunde

def alle_hungrigen_hunde_listen():
  """
  Gibt die Namen aller hungrigen Hunde aus.
  """
  for obj in gc.get_objects():
    if isinstance(obj, Dog):
      if not obj.gefüttert:
        print(f"{obj.name} ist noch hungrig.")