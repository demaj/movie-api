from factory.django import DjangoModelFactory

from datadump.models import Genre, Movie


class GenreFactory(DjangoModelFactory):

    class Meta:
        model = Genre

    name = 'Test Genre'


# class MovieFactory(DjangoModelFactory):
#
#     class Meta:
#         model = Movie
#
#     title = "The Unbearable Lightness of Being"
#     year = 1995
#     genre = GenreFactory()
#     language = 'EN'
#     overview = """
#         Successful surgeon Tomas (Daniel Day-Lewis) leaves Prague for an operation,
#         meets a young photographer named Tereza (Juliette Binoche), and brings her back with him.
#         Tereza is surprised to learn that Tomas is already having an affair with the bohemian Sabina (Lena Olin),
#         but when the Soviet invasion occurs, all three flee to Switzerland. Sabina begins an affair,
#         Tom continues womanizing, and Tereza, disgusted, returns to Czechoslovakia.
#         Realizing his mistake, Tomas decides to chase after her.
#     """
#     rating = 73
