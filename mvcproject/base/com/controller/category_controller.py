from flask import render_template, request, redirect, url_for
from base import app
from base.com.dao.category_dao import CategoryDAO
from base.com.vo.category_vo import CategoryVO

@app.route('/', methods=['GET'])
def admin_home():
    try:
        return render_template("admin/loadCategory.html")
    except Exception as exception:
        print("admin_load_home error>>>>>>>>>>", exception)
        return render_template("admin/viewError.html", error=exception)


@app.route('/admin/add_category', methods=['GET'])
def admin_load_category():
    try:
        return render_template("admin/addCategory.html")
    except Exception as exception:
        print("admin_load_category error>>>>>>>>>>", exception)
        return render_template("admin/viewError.html", error=exception)


@app.route('/admin/insert_category', methods=['POST'])
def admin_insert_category():
    try:
        category_name = request.form.get('categoryName')
        category_description = request.form.get('categoryDescription')

        category_vo = CategoryVO()
        category_dao = CategoryDAO()
        print("-------------------------")

        category_vo.category_name = category_name
        category_vo.category_description = category_description

        category_dao.insert_category(category_vo)

        return redirect("/admin/view_category")
    except Exception as exception:
        print("admin_load_category_add_category error>>>>>>>>>>", exception)
        return render_template("admin/viewError.html", error=exception)


@app.route('/admin/view_category', methods=['GET'])
def admin_view_category():
    try:
        category_dao = CategoryDAO()

        category_list = category_dao.view_category()
        return render_template("admin/viewCategory.html", data=category_list)

    except Exception as exception:
        print("admin_view_category error>>>>>>>>>>", exception)
        return render_template("admin/viewError.html", error=exception)


@app.route("/admin/delete_category",methods=["GET"])
# @login_required('admin')
def admin_delete_category():
    try:
        print("------------------------------------------")
        category_vo = CategoryVO()
        category_dao = CategoryDAO()
        category_id = request.args.get('categoryId')
        print("mj")
        category_vo.category_id = category_id

        category_dao.delete_category(category_vo)

        return redirect('/admin/view_category')
    except Exception as ex:
        print("admin_delete_category route exception occured>>>>>>>>>>", ex)
        return render_template('admin/viewError.html', ex=ex)

@app.route('/admin/edit_category', methods=['GET', 'POST'])
def admin_edit_category():
    try:
        category_id = request.args.get('categoryId')

        category_vo = CategoryVO()
        category_dao = CategoryDAO()

        category_vo.category_id = category_id
        category_list = category_dao.edit_category(category_vo)

        return render_template("admin/updateCategory.html", data=category_list)
    except Exception as exception:
        print("admin_edit_category error>>>>>>>>>>", exception)
        return render_template("admin/viewError.html", error=exception)


@app.route('/admin/update_category', methods=["POST"])
def admin_update_category():
    try:
        category_id = request.form.get('categoryId')
        category_name = request.form.get('categoryName')
        category_description = request.form.get('categoryDescription')
        print("-----------------------")
        category_vo = CategoryVO()
        category_dao = CategoryDAO()

        category_vo.category_id = category_id
        category_vo.category_name = category_name
        category_vo.category_description = category_description

        category_dao.update_category(category_vo)
        print("mj")
        return redirect("/admin/view_category")
    except Exception as exception:
        print("admin_update_category_add_category error>>>>>>>>>>", exception)
        return render_template("admin/viewError.html", error=exception)

