from django.db import models

class BlogPost(models.Model):
    """
    A model representing a blog post.

    Attributes:
        title (str): The title of the blog post.
        content (str): The content of the blog post.
        published_date (datetime): The date and time when the blog post was published.
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns the string representation of the BlogPost instance.

        Returns:
            str: The title of the blog post.
        """
        return self.title
