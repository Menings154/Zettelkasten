from dataclasses import dataclass

@dataclass
class Zettel:
    id: int
    name: str
    summary: str  # will ich das lazy machen, wenn ich performance probleme habe könnte ich das tun?
    text: str  # will ich das lazy machen, wenn ich performance probleme habe könnte ich das tun?

