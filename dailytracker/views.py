from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import TrackerForm
from .models import DailyTracker
from datetime import date
import csv

# Create your views here.
@login_required
def tracker_view(request):
    tracker_inst = DailyTracker(user=request.user, supervisor = request.user.member.all().first().supervisor.username)
    if request.method == "POST":
        form = TrackerForm(request.POST, instance=tracker_inst)
        if form.is_valid():
            form.save()
            return redirect('dailytracker:tracker-home')
    else:
        form = TrackerForm()

    today_claims = request.user.dailytracker_set.filter(date=date.today())
    total_count = len(today_claims)
    context = {
        'form': form,
        'today_claims': today_claims,
        'total_count': total_count,
    }
    return render(request, "dailytracker/index.html", context)

@login_required
def team(request):
    team_members = request.user.supervisor.all()
    team_dict = {}
    for member in team_members:
        team_dict[member.member.username] = len(member.member.dailytracker_set.filter(date=date.today()))
    total_count = 0
    for count in team_dict.values():
        total_count += count

    context = {
        'team_dict': team_dict,
        'total_count': total_count,
    }

    return render(request, "dailytracker/team.html", context)

@login_required
def export_claims_csv(request):
    response = HttpResponse(content_type='text/csv')
    filename = "claims.csv" #Needd to write the filename
    response['Content-Disposition'] = f'attachment; filename={filename}'

    writer = csv.writer(response)
    writer.writerow(['Date', 'AG ID', 'Claim No.', 'Billed Charges', 'Benefit', 'Market', 'Platform', 'Supervisor'])

    datas = request.user.dailytracker_set.all().values_list('date', 'user', 'claim_no', 'billed_charges', 'benefit', 'market', 'platform', 'supervisor')
    for data in datas:
        writer.writerow(data)

    return response