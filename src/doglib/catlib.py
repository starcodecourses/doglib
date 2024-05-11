import gc
import numpy as np

class Cat:
  instances = []
  def __init__(self, name, alter):
    """
    Initialisiert eine neue Katze.

    Args:
        name (str): Der Name der Katze.
        alter (int): Das Alter der Katze.

    Raises:
      TypeError: Wenn einer der Eingabeparameter nicht den erwarteten Typ hat.
    """
    self.__class__.instances.append(self)
    # Enforcing the type of the input parameters
    if not isinstance(name, str):
      raise TypeError("`name` muss vom Typ 'string' sein")
    if not isinstance(alter, int):
      raise TypeError("`alter` muss vom Typ 'integer' sein")
    self.name = name
    self.alter = alter
    # Nicht benutzerinitiierte Attribute
    self.gefüttert = False

  def miezen(self):
    """
    Gibt den Miau-Laut der Katze mit dem entsprechenden Namen aus.
    """
    print(f"Miau! Ich heiße {self.name}.")

  def spielen(self):
    """
    Spielt mit der Katze.
    """
    if np.random.choice([True, False], p=[0.01, 0.99]):
      print(self.name, "wirft eine Vase um. Das wird teuer...")
    else:
      spielobjekt = np.random.choice(["einem Wollknäuel", "einer Maus", "einem Kugelschreiber", "einer Feder"])
      print(self.name, "spielt mit", spielobjekt, "und hat sichtlich Spaß.")

  def füttern(self, futtermenge=1.2):
    """
    Füttert die Katze.

    Args:
        futtermenge (float): Die Menge an Futter in Tassen, die der Katze gegeben wird. Standardwert ist 1.2.
    """
    self.gefüttert = True
    if futtermenge > 1.5:
      print("Das ist zu viel Futter!", self.name, "rollt nun durch die Gegend.")
    elif futtermenge < 1:
      print("Das ist zu wenig Futter!", self.name, "schaut dich hungrig an.")
    else:
      print("Miau! Ich bin nun satt.")

  def umbenennen(self, neuer_name):
    """
    Benennt die Katze um.

    Args:
        neuer_name (str): Der neue Name der Katze.

    Raises:
      TypeError: Wenn der Eingabeparameter nicht den erwarteten Typ hat.
    """
    if not isinstance(neuer_name, str):
      raise TypeError("`neuer_name` muss vom Typ 'string' sein")
    self.name = neuer_name

  def wach(self):
    """
    Überprüft, ob die Katze wach ist.

    Returns:
        bool: True, wenn die Katze wach ist, False sonst.
    """
    return np.random.choice([True, False], p=[10/24, 14/24])

  def alter_in_menschenjahren(self):
    """
    Berechnet das Alter der Katze in Menschenjahren.

    Returns:
        int: Das Alter der Katze in Menschenjahren.
    """
    menschenalter = 24 + (self.alter - 2)*4
    return int(menschenalter)

def umrechnung_futtergewicht_in_tassen(futtergewicht):
  """
  Rechnet das Futtergewicht in Tassen um.

  Args:
      futtergewicht (float): Das Gewicht des Futters in Gramm.

  Returns:
      float: Die Anzahl der Tassen, die dem Futtergewicht entsprechen.
  """
  tassen = futtergewicht/150    # 150g pro Tasse
  return tassen

def alle_katzen():
  """
  Gibt eine Liste aller Katzen-Objekte zurück.

  Returns:
      list: Eine Liste aller Katzen-Objekte.
  """
  katzen = []
  for obj in gc.get_objects():
      if isinstance(obj, Cat):
          katzen.append(obj)
  return katzen

def alle_katzen_listen():
  """
  Gibt die Namen aller Katzen aus.
  """
  for obj in gc.get_objects():
      if isinstance(obj, Cat):
          print(obj.name)

def alle_hungrigen_katzen_listen():
  """
  Gibt eine Liste aller hungrigen Katzen-Objekte zurück.

  Returns:
      list: Eine Liste aller hungrigen Katzen-Objekte.
  """
  hungrige_katzen = []
  for obj in gc.get_objects():
      if isinstance(obj, Cat):
          if not obj.gefüttert:
            hungrige_katzen.append(obj)
  return hungrige_katzen

def alle_hungrigen_katzen_listen():
  """
  Gibt die Namen aller hungrigen Katzen aus.
  """
  for obj in gc.get_objects():
      if isinstance(obj, Cat):
          if not obj.gefüttert:
            print(f"{obj.name} ist noch hungrig.")