import os
from flask import request, redirect, url_for, flash, render_template, abort, current_app
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user
from myapp.models import GalleryImage
from myapp.extensions import db
from myapp.admin import bp  # questo è il Blueprint corretto

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/gallery/upload', methods=['GET', 'POST'])  # usa bp, non admin_bp
@login_required
def upload_gallery_image():
    if not current_user.is_admin:
        abort(403)
    
    if request.method == 'POST':
        file = request.files.get('image')
        if not file or file.filename == '':
            flash('Nessun file selezionato', 'danger')
            return redirect(request.url)
        
        if allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_folder = current_app.config['UPLOAD_FOLDER']
            file.save(os.path.join(upload_folder, filename))
            
            alt_text = request.form.get('alt_text', '')
            new_img = GalleryImage(filename=filename, alt_text=alt_text)
            db.session.add(new_img)
            db.session.commit()
            
            flash('Immagine caricata!', 'success')
            return redirect(url_for('admin.admin_gallery_list'))
    
    return render_template('admin_upload.html')

@bp.route('/gallery')
@login_required
def admin_gallery_list():
    if not current_user.is_admin:
        abort(403)
    images = GalleryImage.query.order_by(GalleryImage.upload_date.desc()).all()
    return render_template('admin_gallery_list.html', images=images)

@bp.route('/gallery/delete/<int:image_id>', methods=['POST'])
@login_required
def admin_gallery_delete(image_id):
    if not current_user.is_admin:
        abort(403)
    img = GalleryImage.query.get_or_404(image_id)
    path = os.path.join(current_app.config['UPLOAD_FOLDER'], img.filename)
    
    try:
        os.remove(path)
    except FileNotFoundError:
        pass
    
    db.session.delete(img)
    db.session.commit()
    flash('Immagine rimossa', 'success')
    return redirect(url_for('admin.admin_gallery_list'))
