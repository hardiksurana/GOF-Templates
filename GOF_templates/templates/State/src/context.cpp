#include "../include/mobile.h"

{% for fn in functions %}
	{{fn.return}} Context::{{fn.name}}({{fn.params}}) {
		_ptr_state->{{fn.name}}({{fn.params}});
	}
{% endfor %}

Context::Context() {
}

Mobile::~Mobile() {

}