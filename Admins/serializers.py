from rest_framework import serializers
from .models import *
from utils import *

# serializers for the models in the Admins app
class AdminSerializer(serializers.ModelSerializer):
    school = serializers.SerializerMethodField()
    headshot = serializers.SerializerMethodField()
    headshot_url = serializers.SerializerMethodField()
    headshot_name = serializers.SerializerMethodField()
    class Meta:
        model = Administrator
        fields = '__all__'

    def get_school(self, obj):
        return {'id': obj.school.id, 'name': obj.school.Schoolname}
    
    def get_headshot_url(self, obj):
        return get_full_image_url(obj.headshot)
    
    def get_headshot_name(self, obj):
        return get_image_name(obj.headshot)

# serializer for the school model
class SchoolSerializer(serializers.ModelSerializer):
    sessions = serializers.SerializerMethodField()
    classes = serializers.SerializerMethodField()
    subjects = serializers.SerializerMethodField()
    Schoollogo = serializers.SerializerMethodField()
    Schoollogo_url = serializers.SerializerMethodField()
    Schoollogo_name = serializers.SerializerMethodField()
    num_students = serializers.SerializerMethodField()
    num_teachers = serializers.SerializerMethodField()

    class Meta:
        model = School
        exclude = ['session', 'Subjects']


    def get_sessions(self, obj):
        session_data = obj.session.all()
        sessions = []
        for session in session_data:
            terms = session.terms.all()  # Assuming a ForeignKey relationship from Term to Session
            session_obj = {
                "id": session.id,
                "session": session.session,
                "terms": [{"id": term.id, "term": term.term} for term in terms]
            }
            sessions.append(session_obj)
        return sessions

    
    def get_classes(self, obj):
        classes_data = obj.classes.all()
        return [{"id":class_.id,"class":class_.Class} for class_ in classes_data]
    
    def get_subjects(self, obj):
        subjects_data = obj.Subjects.all()
        return [{"id":subject.id,"subject":subject.subject_name} for subject in subjects_data]
    
    def get_Schoollogo_url(self, obj):
        return get_full_image_url(obj.Schoollogo)
    
    def get_Schoollogo_name(self, obj):
        return get_image_name(obj.Schoollogo)

    def get_num_students(self, obj):
        return obj.student_set.count()

    def get_num_teachers(self, obj):
        return obj.teacher_set.count()


# serializer for the academic session model
class AcademicSessionSerializer(serializers.ModelSerializer):
    terms = serializers.SerializerMethodField()
    class Meta:
        model = AcademicSession
        fields = '__all__'
    
    def get_terms(self, obj):
        terms_data = obj.terms.all()
        return [{"id":term.id,"term":term.term} for term in terms_data]

# serializer for the term model
class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = '__all__'

# serializer for the class model
class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

# serializer for the subject model
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

# serializer for the subject allocation model
class SubjectallocationSerializer(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()
    classname = serializers.SerializerMethodField()
    school = serializers.SerializerMethodField()
    class Meta:
        model = Subjectallocation
        fields = '__all__' 

    def get_subjects(self, obj):
        subjects_data = obj.subjects.all()
        return [{"id":subject.id,"name":subject.subject_name} for subject in subjects_data]

    def get_classname(self, obj):
        return{'id': obj.classname.id, 'name': obj.classname.Class}
    
    def get_school(self, obj):
        return {'id': obj.school.id, 'name': obj.school.Schoolname}
    

class NewsletterSerializer(serializers.ModelSerializer):
    session = serializers.SerializerMethodField()
    term = serializers.SerializerMethodField()
    class Meta:
        model = Newsletter
        fields = '__all__'

    def get_session(self, obj):
        return {'id': obj.Newslettersession.id, 'name': obj.Newslettersession.session}
    
    def get_term(self, obj):
        return {'id': obj.Newsletterterm.id, 'name': obj.Newsletterterm.term}

    
class NotificationSerializer(serializers.ModelSerializer):
    school = serializers.SerializerMethodField()
    class Meta:
        model = Notification
        fields = '__all__'

    def get_school(self, obj):
        return {'id': obj.school.id, 'name': obj.school.Schoolname}
    