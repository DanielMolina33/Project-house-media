# Cloudinary functions

# Cloudinary
import cloudinary

class CloudinaryFunctions:
    @staticmethod
    def upload(file):
        result = cloudinary.uploader.upload(
            file,
            folder = 'Django'
        )
        return result


    @staticmethod
    def update(file, id):
        result = cloudinary.uploader.upload(
            file,
            public_id = id,
            overwrite = True
        )
        return result


    @staticmethod
    def delete(id):
        result = cloudinary.uploader.destroy(
            public_id = id
        )

        return result
