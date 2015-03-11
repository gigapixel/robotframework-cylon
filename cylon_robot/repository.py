import re
import glob
import yaml

from .log import *


class repository:
    refs = None
    ref_root = ''
    ref_leaf = ''

    @classmethod
    def load_references(cls, files="./repositories/*.yml"):
        cls.refs = {}
        for filename in glob.glob(files):
            doc = yaml.load(open(filename))
            cls.refs.update(doc)

    @classmethod
    def extract_ref(cls, ref):
        if ref.startswith('...'):
            ref = cls.ref_leaf + ref[ref.rfind('.'):]
        elif ref.startswith('.'):
            ref = cls.ref_root + ref

        if "'" not in ref:
            cls.ref_root = ref[:ref.find('.')]
            cls.ref_leaf = ref[:ref.rfind('.')]

        return cls.get_ref_value(ref)

    @classmethod
    def get_ref_value(cls, ref):
        if ref.startswith("'") and ref.endswith("'"):
            value = ref[1:-1]
        else:
            nodes = ref.split('.')
            refs = cls.refs

            try:
                for node in nodes:
                    if node != nodes[-1]:
                        refs = refs[node]
                    else:
                        value = refs[node]
            except KeyError:
                log.error("ref not found: %s" % ref)

        return cls.replace_refs(value)


    @classmethod
    def replace_refs(cls, text):
        pattern = '#{([^}]*)}'
        refs = re.findall(pattern, text)

        for ref in refs:
            value = cls.get_ref_value(ref)
            variable = "#{%s}" % ref
            text = text.replace(variable, value)

        return text
