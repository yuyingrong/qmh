
# not sure why this script does not work
# use the other script that produces graph by JS instead

import plotly
import plotly.graph_objs as go
from qmh.models import Patient

rawAdmitYear = [p.admitYear for p in Patient.objects.all()]
rawAdmitAge = [p.admitAge for p in Patient.objects.all()]
rawFirstName = [p.firstName for p in Patient.objects.all()]
rawLastName = [p.lastName for p in Patient.objects.all()]
admitYear = []
admitAge = []
firstName = []
lastName = []
for (y, a, f, l) in zip(rawAdmitYear, rawAdmitAge, rawFirstName, rawLastName):
        if not y == '' and not a == 0:
                admitYear.append(y)
                admitAge.append(a)
                firstName.append(f)
                lastName.append(l)

# Of all 2208 patient entries,
# 336 entries either have empty year entry ('') or have zero age entry (0),
# leaving only 1872 valid points entered for making the scatterplot.

names = []
for (f, l) in zip(firstName, lastName):
        names.append(f+' '+l)

fig = go.Figure(data=go.Scatter(x=admitYear,
                                y=admitAge,
                                mode='markers',
                                marker_color=admitAge,
                                text=names))

fig.update_layout(title='Patient Age at Admission vs. Year of Admission Scatterplot')
plotly.offline.plot(fig, filename='../qmh/static/images/Scatter.html', auto_open=False)


