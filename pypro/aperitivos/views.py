from django.shortcuts import render

videos = [
    {'slug': 'motivacao', 'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': 447357180},
    {'slug': 'instalacao-windows', 'titulo': 'Instalação Windows', 'vimeo_id': 452956335},
]

videos_dct = {dct['slug']: dct for dct in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
