string1 = """
GK ['Alisson', 'Adrián', 'Caoimhin Kelleher', 'Mohamed Salah', 'Virgil van Dijk', 'Jordan Henderson', 'Georginio Wijnaldum', 'Sadio Mané', 'Trent Alexander-Arnold', 'Andrew Robertson', 'Fabinho', 'Naby Keïta', 'Thiago', 'Diogo Jota', 'Xherdan Shaqiri', 'Alex Oxlade-Chamberlain', 'James Milner', 'Roberto Firmino', 'Divock Origi', 'Joel Matip', 'Konstantinos Tsimikas', 'Joe Gomez', 'Ben Davies', 'Neco Williams', 'Curtis Jones', 'Ozan Kabak', 'Rhys Williams', 'Ben Woodburn', 'Nathaniel Phillips', 'Paul Glatzel', 'Billy Koumetio', 'Yasser Larouci', 'Joe Hardy']
RB ['Andrew Robertson', 'Trent Alexander-Arnold', 'Fabinho', 'Virgil van Dijk', 'Jordan Henderson', 'Georginio Wijnaldum', 'James Milner', 'Joe Gomez', 'Thiago', 'Konstantinos Tsimikas', 'Joel Matip', 'Alex Oxlade-Chamberlain', 'Roberto Firmino', 'Naby Keïta', 'Ben Davies', 'Mohamed Salah', 'Diogo Jota', 'Sadio Mané', 'Ozan Kabak', 'Neco Williams', 'Curtis Jones', 'Xherdan Shaqiri', 'Nathaniel Phillips', 'Yasser Larouci', 'Rhys Williams', 'Divock Origi', 'Billy Koumetio', 'Ben Woodburn', 'Paul Glatzel', 'Joe Hardy', 'Alisson', 'Adrián', 'Caoimhin Kelleher']
CB ['Virgil van Dijk', 'Fabinho', 'Joel Matip', 'Jordan Henderson', 'Joe Gomez', 'Georginio Wijnaldum', 'Andrew Robertson', 'Trent Alexander-Arnold', 'James Milner', 'Ozan Kabak', 'Ben Davies', 'Thiago', 'Konstantinos Tsimikas', 'Alex Oxlade-Chamberlain', 'Roberto Firmino', 'Nathaniel Phillips', 'Naby Keïta', 'Diogo Jota', 'Curtis Jones', 'Sadio Mané', 'Mohamed Salah', 'Rhys Williams', 'Neco Williams', 'Xherdan Shaqiri', 'Yasser Larouci', 'Billy Koumetio', 'Divock Origi', 'Paul Glatzel', 'Ben Woodburn', 'Joe Hardy', 'Alisson', 'Adrián', 'Caoimhin Kelleher']
LB ['Andrew Robertson', 'Trent Alexander-Arnold', 'Fabinho', 'Virgil van Dijk', 'Jordan Henderson', 'Georginio Wijnaldum', 'James Milner', 'Joe Gomez', 'Thiago', 'Konstantinos Tsimikas', 'Joel Matip', 'Alex Oxlade-Chamberlain', 'Roberto Firmino', 'Naby Keïta', 'Ben Davies', 'Diogo Jota', 'Mohamed Salah', 'Sadio Mané', 'Ozan Kabak', 'Neco Williams', 'Curtis Jones', 'Xherdan Shaqiri', 'Nathaniel Phillips', 'Yasser Larouci', 'Rhys Williams', 'Divock Origi', 'Billy Koumetio', 'Ben Woodburn', 'Paul Glatzel', 'Joe Hardy', 'Alisson', 'Adrián', 'Caoimhin Kelleher']
CDM ['Fabinho', 'Jordan Henderson', 'Georginio Wijnaldum', 'Virgil van Dijk', 'Trent Alexander-Arnold', 'Andrew Robertson', 'James Milner', 'Thiago', 'Joel Matip', 'Alex Oxlade-Chamberlain', 'Joe Gomez', 'Naby Keïta', 'Roberto Firmino', 'Konstantinos Tsimikas', 'Diogo Jota', 'Ozan Kabak', 'Mohamed Salah', 'Ben Davies', 'Curtis Jones', 'Sadio Mané', 'Xherdan Shaqiri', 'Nathaniel Phillips', 'Neco Williams', 'Rhys Williams', 'Yasser Larouci', 'Divock Origi', 'Billy Koumetio', 'Ben Woodburn', 'Paul Glatzel', 'Joe Hardy', 'Alisson', 'Adrián', 'Caoimhin Kelleher']
CM ['Georginio Wijnaldum', 'Thiago', 'Jordan Henderson', 'Trent Alexander-Arnold', 'Fabinho', 'Roberto Firmino', 'Mohamed Salah', 'James Milner', 'Andrew Robertson', 'Sadio Mané', 'Naby Keïta', 'Alex Oxlade-Chamberlain', 'Diogo Jota', 'Virgil van Dijk', 'Xherdan Shaqiri', 'Curtis Jones', 'Joel Matip', 'Konstantinos Tsimikas', 'Joe Gomez', 'Divock Origi', 'Ozan Kabak', 'Ben Davies', 'Neco Williams', 'Ben Woodburn', 'Yasser Larouci', 'Rhys Williams', 'Nathaniel Phillips', 'Paul Glatzel', 'Billy Koumetio', 'Joe Hardy', 'Alisson', 'Adrián', 'Caoimhin Kelleher']
CF ['Mohamed Salah', 'Sadio Mané', 'Roberto Firmino', 'Diogo Jota', 'Georginio Wijnaldum', 'Thiago', 'Jordan Henderson', 'Trent Alexander-Arnold', 'Naby Keïta', 'Alex Oxlade-Chamberlain', 'Andrew Robertson', 'Xherdan Shaqiri', 'Fabinho', 'James Milner', 'Divock Origi', 'Curtis Jones', 'Virgil van Dijk', 'Konstantinos Tsimikas', 'Joel Matip', 'Ben Woodburn', 'Joe Gomez', 'Ozan Kabak', 'Paul Glatzel', 'Neco Williams', 'Yasser Larouci', 'Ben Davies', 'Joe Hardy', 'Rhys Williams', 'Nathaniel Phillips', 'Billy Koumetio', 'Alisson', 'Adrián', 'Caoimhin Kelleher']
RW ['Mohamed Salah', 'Sadio Mané', 'Roberto Firmino', 'Diogo Jota', 'Georginio Wijnaldum', 'Thiago', 'Trent Alexander-Arnold', 'Jordan Henderson', 'Xherdan Shaqiri', 'Alex Oxlade-Chamberlain', 'Andrew Robertson', 'Naby Keïta', 'Fabinho', 'James Milner', 'Divock Origi', 'Konstantinos Tsimikas', 'Curtis Jones', 'Virgil van Dijk', 'Joe Gomez', 'Ben Woodburn', 'Joel Matip', 'Neco Williams', 'Ben Davies', 'Yasser Larouci', 'Paul Glatzel', 'Ozan Kabak', 'Joe Hardy', 'Rhys Williams', 'Nathaniel Phillips', 'Billy Koumetio', 'Alisson', 'Adrián', 'Caoimhin Kelleher']
LW ['Sadio Mané', 'Mohamed Salah', 'Roberto Firmino', 'Diogo Jota', 'Georginio Wijnaldum', 'Thiago', 'Trent Alexander-Arnold', 'Jordan Henderson', 'Xherdan Shaqiri', 'Alex Oxlade-Chamberlain', 'Andrew Robertson', 'Naby Keïta', 'Fabinho', 'James Milner', 'Divock Origi', 'Konstantinos Tsimikas', 'Curtis Jones', 'Virgil van Dijk', 'Joe Gomez', 'Ben Woodburn', 'Joel Matip', 'Neco Williams', 'Ben Davies', 'Yasser Larouci', 'Paul Glatzel', 'Ozan Kabak', 'Joe Hardy', 'Rhys Williams', 'Nathaniel Phillips', 'Billy Koumetio', 'Alisson', 'Adrián', 'Caoimhin Kelleher']
"""

string2 = """
GK ['Alisson', 'Adrián', 'Caoimhin Kelleher', 'Mohamed Salah', 'Virgil van Dijk', 'Jordan Henderson', 'Georginio Wijnaldum', 'Sadio Mané', 'Trent Alexander-Arnold', 'Andrew Robertson', 'Fabinho', 'Naby Keïta', 'Thiago', 'Diogo Jota', 'Xherdan Shaqiri', 'Alex Oxlade-Chamberlain', 'James Milner', 'Roberto Firmino', 'Divock Origi', 'Joel Matip', 'Konstantinos Tsimikas', 'Joe Gomez', 'Ben Davies', 'Neco Williams', 'Curtis Jones', 'Ozan Kabak', 'Rhys Williams', 'Ben Woodburn', 'Nathaniel Phillips', 'Paul Glatzel', 'Billy Koumetio', 'Yasser Larouci', 'Joe Hardy']
RB ['Andrew Robertson', 'Trent Alexander-Arnold', 'Fabinho', 'Virgil van Dijk', 'Jordan Henderson', 'Georginio Wijnaldum', 'James Milner', 'Joe Gomez', 'Thiago', 'Konstantinos Tsimikas', 'Joel Matip', 'Alex Oxlade-Chamberlain', 'Roberto Firmino', 'Naby Keïta', 'Ben Davies', 'Mohamed Salah', 'Diogo Jota', 'Sadio Mané', 'Ozan Kabak', 'Neco Williams', 'Curtis Jones', 'Xherdan Shaqiri', 'Nathaniel Phillips', 'Yasser Larouci', 'Rhys Williams', 'Divock Origi', 'Billy Koumetio', 'Ben Woodburn', 'Paul Glatzel', 'Joe Hardy', 'Alisson', 'Adrián', 'Caoimhin Kelleher']
CB ['Virgil van Dijk', 'Fabinho', 'Joel Matip', 'Jordan Henderson', 'Joe Gomez', 'Georginio Wijnaldum', 'Andrew Robertson', 'Trent Alexander-Arnold', 'James Milner', 'Ozan Kabak', 'Ben Davies', 'Thiago', 'Konstantinos Tsimikas', 'Alex Oxlade-Chamberlain', 'Roberto Firmino', 'Nathaniel Phillips', 'Naby Keïta', 'Diogo Jota', 'Curtis Jones', 'Sadio Mané', 'Mohamed Salah', 'Rhys Williams', 'Neco Williams', 'Xherdan Shaqiri', 'Yasser Larouci', 'Billy Koumetio', 'Divock Origi', 'Paul Glatzel', 'Ben Woodburn', 'Joe Hardy', 'Alisson', 'Adrián', 'Caoimhin Kelleher']
LB ['Andrew Robertson', 'Trent Alexander-Arnold', 'Fabinho', 'Virgil van Dijk', 'Jordan Henderson', 'Georginio Wijnaldum', 'James Milner', 'Joe Gomez', 'Thiago', 'Konstantinos Tsimikas', 'Joel Matip', 'Alex Oxlade-Chamberlain', 'Roberto Firmino', 'Naby Keïta', 'Ben Davies', 'Diogo Jota', 'Mohamed Salah', 'Sadio Mané', 'Ozan Kabak', 'Neco Williams', 'Curtis Jones', 'Xherdan Shaqiri', 'Nathaniel Phillips', 'Yasser Larouci', 'Rhys Williams', 'Divock Origi', 'Billy Koumetio', 'Ben Woodburn', 'Paul Glatzel', 'Joe Hardy', 'Alisson', 'Adrián', 'Caoimhin Kelleher']
CDM ['Fabinho', 'Jordan Henderson', 'Georginio Wijnaldum', 'Virgil van Dijk', 'Trent Alexander-Arnold', 'Andrew Robertson', 'James Milner', 'Thiago', 'Joel Matip', 'Alex Oxlade-Chamberlain', 'Joe Gomez', 'Naby Keïta', 'Roberto Firmino', 'Konstantinos Tsimikas', 'Diogo Jota', 'Ozan Kabak', 'Mohamed Salah', 'Ben Davies', 'Curtis Jones', 'Sadio Mané', 'Xherdan Shaqiri', 'Nathaniel Phillips', 'Neco Williams', 'Rhys Williams', 'Yasser Larouci', 'Divock Origi', 'Billy Koumetio', 'Ben Woodburn', 'Paul Glatzel', 'Joe Hardy', 'Alisson', 'Adrián', 'Caoimhin Kelleher']
CM ['Georginio Wijnaldum', 'Thiago', 'Jordan Henderson', 'Trent Alexander-Arnold', 'Fabinho', 'Roberto Firmino', 'Mohamed Salah', 'James Milner', 'Andrew Robertson', 'Sadio Mané', 'Naby Keïta', 'Alex Oxlade-Chamberlain', 'Diogo Jota', 'Virgil van Dijk', 'Xherdan Shaqiri', 'Curtis Jones', 'Joel Matip', 'Konstantinos Tsimikas', 'Joe Gomez', 'Divock Origi', 'Ozan Kabak', 'Ben Davies', 'Neco Williams', 'Ben Woodburn', 'Yasser Larouci', 'Rhys Williams', 'Nathaniel Phillips', 'Paul Glatzel', 'Billy Koumetio', 'Joe Hardy', 'Alisson', 'Adrián', 'Caoimhin Kelleher']
CF ['Mohamed Salah', 'Sadio Mané', 'Roberto Firmino', 'Diogo Jota', 'Georginio Wijnaldum', 'Thiago', 'Jordan Henderson', 'Trent Alexander-Arnold', 'Naby Keïta', 'Alex Oxlade-Chamberlain', 'Andrew Robertson', 'Xherdan Shaqiri', 'Fabinho', 'James Milner', 'Divock Origi', 'Curtis Jones', 'Virgil van Dijk', 'Konstantinos Tsimikas', 'Joel Matip', 'Ben Woodburn', 'Joe Gomez', 'Ozan Kabak', 'Paul Glatzel', 'Neco Williams', 'Yasser Larouci', 'Ben Davies', 'Joe Hardy', 'Rhys Williams', 'Nathaniel Phillips', 'Billy Koumetio', 'Alisson', 'Adrián', 'Caoimhin Kelleher']
RW ['Mohamed Salah', 'Sadio Mané', 'Roberto Firmino', 'Diogo Jota', 'Georginio Wijnaldum', 'Thiago', 'Trent Alexander-Arnold', 'Jordan Henderson', 'Xherdan Shaqiri', 'Alex Oxlade-Chamberlain', 'Andrew Robertson', 'Naby Keïta', 'Fabinho', 'James Milner', 'Divock Origi', 'Konstantinos Tsimikas', 'Curtis Jones', 'Virgil van Dijk', 'Joe Gomez', 'Ben Woodburn', 'Joel Matip', 'Neco Williams', 'Ben Davies', 'Yasser Larouci', 'Paul Glatzel', 'Ozan Kabak', 'Joe Hardy', 'Rhys Williams', 'Nathaniel Phillips', 'Billy Koumetio', 'Alisson', 'Adrián', 'Caoimhin Kelleher']
LW ['Sadio Mané', 'Mohamed Salah', 'Roberto Firmino', 'Diogo Jota', 'Georginio Wijnaldum', 'Thiago', 'Trent Alexander-Arnold', 'Jordan Henderson', 'Xherdan Shaqiri', 'Alex Oxlade-Chamberlain', 'Andrew Robertson', 'Naby Keïta', 'Fabinho', 'James Milner', 'Divock Origi', 'Konstantinos Tsimikas', 'Curtis Jones', 'Virgil van Dijk', 'Joe Gomez', 'Ben Woodburn', 'Joel Matip', 'Neco Williams', 'Ben Davies', 'Yasser Larouci', 'Paul Glatzel', 'Ozan Kabak', 'Joe Hardy', 'Rhys Williams', 'Nathaniel Phillips', 'Billy Koumetio', 'Alisson', 'Adrián', 'Caoimhin Kelleher']
"""

{'Alisson': ['GK'], 'Andrew Robertson': ['RB', 'LB'], 'Virgil van Dijk': ['RCB', 'LCB'], 'Fabinho': ['CDM', 'RB', 'LB', 'RCB', 'LCB'], 'Georginio Wijnaldum': ['RCM', 'LCM'], 'Mohamed Salah': ['CF', 'RW', 'LW'], 'Sadio Mané': ['LW', 'CF', 'RW'], 'Trent Alexander-Arnold': ['RB', 'LB'], 'Jordan Henderson': ['CDM'], 'Thiago': ['RCM', 'LCM']}


[['Goalkeeper'], ['Outside Back'], ['Center Back'], ['Outside Back', 'Defensive Midfielder', 'Center Back'], ['Center Midfielder'], ['Winger', 'Forward'], ['Winger', 'Forward'], ['Outside Back'], ['Defensive Midfielder'], ['Center Midfielder']] ITERARRAY


{'Joel Matip': ['RCB'], 'Roberto Firmino': ['CF'], 'Joe Gomez': ['RCB'], 'Diogo Jota': ['CF']}


[['Center Back'], ['Forward'], ['Center Back'], ['Forward']] ITERARRAY





{'Alisson': ['GK'], 'Andrew Robertson': ['RB', 'LB'], 'Virgil van Dijk': ['RCB', 'LCB'], 'Fabinho': ['CDM', 'RB', 'LB', 'RCB', 'LCB'], 'Georginio Wijnaldum': ['RCM', 'LCM'], 'Mohamed Salah': ['CF', 'RW', 'LW'], 'Sadio Mané': ['LW', 'CF', 'RW'], 'Trent Alexander-Arnold': ['RB', 'LB'], 'Jordan Henderson': ['CDM'], 'Thiago': ['RCM', 'LCM']}


[['Goalkeeper'], ['Outside Back'], ['Center Back'], ['Defensive Midfielder', 'Center Back', 'Outside Back'], ['Center Midfielder'], ['Forward', 'Winger'], ['Forward', 'Winger'], ['Outside Back'], ['Defensive Midfielder'], ['Center Midfielder']] ITERARRAY


{'Joel Matip': ['RCB'], 'Roberto Firmino': ['RW', 'LW'], 'Jordan Henderson': ['RCB'], 'Diogo Jota': ['RW', 'LW']}


[['Center Back'], ['Winger'], ['Center Back'], ['Winger']] ITERARRAY


{'Diogo Jota': ['RW'], 'Thiago': ['RW']}


[['Winger'], ['Winger']] ITERARRAY

















['Alisson', 'Andrew Robertson', 'Virgil van Dijk', 'Fabinho', 'Georginio Wijnaldum', 'Mohamed Salah', 'Sadio Mané', 'Trent Alexander-Arnold', 'Jordan Henderson', 'Thiago']

BEST
('Goalkeeper', 'Outside Back', 'Center Back', 'Center Back', 'Center Midfielder', 'Winger', 'Winger', 'Outside Back', 'Defensive Midfielder', 'Center Midfielder')
874


BEST
('Goalkeeper', 'Outside Back', 'Center Back', 'Defensive Midfielder', 'Center Midfielder', 'Winger', 'Winger', 'Outside Back', 'Defensive Midfielder', 'Center Midfielder')
876

['Joel Matip', 'Roberto Firmino', 'Joe Gomez', 'Diogo Jota']

BEST
('Center Back', 'Forward')
169












['Alisson', 'Andrew Robertson', 'Virgil van Dijk', 'Fabinho', 'Georginio Wijnaldum', 'Mohamed Salah', 'Sadio Mané', 'Trent Alexander-Arnold', 'Jordan Henderson', 'Thiago']

BEST
('Goalkeeper', 'Outside Back', 'Center Back', 'Center Back', 'Center Midfielder', 'Forward', 'Forward', 'Outside Back', 'Defensive Midfielder', 'Center Midfielder')
874


BEST

('Goalkeeper', 'Outside Back', 'Center Back', 'Defensive Midfielder', 'Center Midfielder', 'Forward', 'Forward', 'Outside Back', 'Defensive Midfielder', 'Center Midfielder')
876

['Joel Matip', 'Roberto Firmino', 'Jordan Henderson', 'Diogo Jota']

BEST
('Center Back', 'Winger', 'Center Back')
250

['Diogo Jota', 'Thiago']

BEST
('Winger',)
83















print(string1==string2)
